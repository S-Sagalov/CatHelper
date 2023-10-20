from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models.charity_project import CharityProject
from app.schemas.charity_project import CharityProjectUpdate


async def check_name_is_unique(project_name: str,
                               session: AsyncSession) -> CharityProject:
    project = await charity_project_crud.get_project_by_name(project_name,
                                                             session)
    if project:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Проект с таким именем уже существует!',
        )


async def get_existing_project_by_id(project_id: int,
                                     session: AsyncSession) -> CharityProject:
    project = await charity_project_crud.get(project_id, session)
    if not project:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f'Проект с id {project_id} не найден!'
        )
    return project


async def project_not_close(project: CharityProject) -> None:
    if project.fully_invested:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='Закрытый проект нельзя редактировать!')


async def amount_not_less_then_available(project: CharityProject,
                                         new_data: CharityProjectUpdate
                                         ) -> None:
    if new_data.full_amount and project.invested_amount > new_data.full_amount:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='Сумма не должна быть меньше внесённой!')


async def project_have_money(project: CharityProject) -> None:
    if project.invested_amount:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='В проект были внесены средства, '
                                   'не подлежит удалению!')

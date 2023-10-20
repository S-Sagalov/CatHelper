from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.services import invest_to_object
from app.api.validators import (check_name_is_unique,
                                get_existing_project_by_id,
                                project_not_close,
                                amount_not_less_then_available,
                                project_have_money)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.schemas.charity_project import (
    CharityProjectUpdate, CharityProjectDB, CharityProjectCreate
)

router = APIRouter()


@router.get('/',
            response_model=list[CharityProjectDB],
            response_model_exclude_none=True)
async def get_all_project(session: AsyncSession = Depends(get_async_session)):
    return await charity_project_crud.get_multi(session)


@router.post('/',
             response_model=CharityProjectDB,
             response_model_exclude_none=True,
             dependencies=[Depends(current_superuser)]
             )
async def create_project(project: CharityProjectCreate,
                         session: AsyncSession = Depends(get_async_session)):
    await check_name_is_unique(project.name, session)
    new_project = await charity_project_crud.create(project, session)
    return await invest_to_object(new_project, session)


@router.patch('/{project_id}',
              response_model=CharityProjectDB,
              dependencies=[Depends(current_superuser)]
              )
async def update_project(project_id: int,
                         project_data: CharityProjectUpdate,
                         session: AsyncSession = Depends(get_async_session)):
    project = await get_existing_project_by_id(project_id, session)
    await project_not_close(project)
    await amount_not_less_then_available(project, project_data)
    if project_data.name:
        await check_name_is_unique(project_data.name, session)
    project = await charity_project_crud.update(project, project_data, session)
    return await invest_to_object(project, session)


@router.delete('/{project_id}',
               response_model=CharityProjectDB,
               dependencies=[Depends(current_superuser)]
               )
async def delete_project(project_id: int,
                         session: AsyncSession = Depends(get_async_session)):
    project = await get_existing_project_by_id(project_id, session)
    await project_have_money(project)
    return await charity_project_crud.delete(project, session)

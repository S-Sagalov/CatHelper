from typing import Optional

from sqlalchemy import select, desc, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):
    async def get_project_by_name(self, project_name: str,
                                  session: AsyncSession
                                  ) -> Optional[CharityProject]:
        project = await session.execute(
            select(CharityProject).where(CharityProject.name == project_name))
        project = project.scalars().first()
        return project

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession) -> Optional[list[CharityProject]]:
        projects = await session.execute(
            select([CharityProject.name, (
                    func.julianday(CharityProject.close_date) -
                    func.julianday(CharityProject.create_date)
                    ).label('life_time'),
                    CharityProject.description]).where(
                CharityProject.fully_invested).order_by(
                desc('life_time'))
        )
        projects = projects.all()
        return projects


charity_project_crud = CRUDCharityProject(CharityProject)

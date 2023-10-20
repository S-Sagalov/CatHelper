from aiogoogle import Aiogoogle
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.services.google_api import (spreadsheets_create,
                                         set_user_permissions,
                                         spreadsheets_update_value)
from app.core.db import get_async_session
from app.core.google_client import get_service
from app.core.user import current_superuser

from app.crud.charity_project import charity_project_crud

router = APIRouter()


@router.get('/',
            dependencies=[Depends(current_superuser)]
            )
async def get_closed_projects_table(
        session: AsyncSession = Depends(get_async_session),
        wrapper_services: Aiogoogle = Depends(get_service)):
    projects = await charity_project_crud.get_projects_by_completion_rate(
        session)
    spreadsheet_id = await spreadsheets_create(wrapper_services)
    await set_user_permissions(spreadsheet_id, wrapper_services)
    await spreadsheets_update_value(spreadsheet_id,
                                    projects,
                                    wrapper_services)

    return {
        'ссылка на документ':
            f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}'}

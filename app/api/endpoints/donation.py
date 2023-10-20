from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.services import invest_to_object
from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models import User
from app.schemas.donation import (DonationCreate,
                                  DonationDBForUser,
                                  DonationDBForAdmin)

router = APIRouter()


@router.post('/',
             response_model=DonationDBForUser,
             response_model_exclude_none=True)
async def create_donation(donation: DonationCreate,
                          session: AsyncSession = Depends(
                              get_async_session),
                          user: User = Depends(current_user)):
    donation = await donation_crud.create(donation, session, user)
    return await invest_to_object(donation, session)


@router.get('/',
            response_model=list[DonationDBForAdmin],
            response_model_exclude_none=True,
            dependencies=[Depends(current_superuser)]
            )
async def get_all_donations(
        session: AsyncSession = Depends(get_async_session)):
    return await donation_crud.get_multi(session)


@router.get('/my', response_model=list[DonationDBForUser],
            response_model_exclude={'user_id'})
async def get_all_user_donations(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)):
    return await donation_crud.get_user_donations(user, session)

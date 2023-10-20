from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import User
from app.models.donation import Donation


class CRUDDonation(CRUDBase):
    async def get_user_donations(self,
                                 user: User,
                                 session: AsyncSession):
        donation = await session.execute(
            select(Donation).where(Donation.user_id == user.id))
        donation = donation.scalars().all()
        return donation


donation_crud = CRUDDonation(Donation)

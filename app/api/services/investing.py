from datetime import datetime
from typing import List, Union

from sqlalchemy import select, false
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation

MODELS = {
    Donation: CharityProject,
    CharityProject: Donation
}


async def get_all_not_closed_objects(
        model: Union[CharityProject, Donation],
        session: AsyncSession
) -> List[Union[CharityProject, Donation]]:
    db_objects = await session.execute(
        select(model).where(
            model.fully_invested == false()).order_by(model.create_date)
    )
    return db_objects.scalars().all()


async def close_invested_object(closed_object: Union[CharityProject, Donation],
                                ) -> None:
    closed_object.close_date = datetime.now()
    closed_object.fully_invested = True


async def invest_to_object(
        object_in: Union[CharityProject, Donation],
        session: AsyncSession
) -> Union[CharityProject, Donation]:
    model = MODELS[object_in.__class__]
    not_invested_objects = await get_all_not_closed_objects(model, session)
    if not not_invested_objects:
        return object_in

    available_amount = object_in.full_amount

    for obj_for_invest in not_invested_objects:
        needed_amount = (
            obj_for_invest.full_amount - obj_for_invest.invested_amount)

        to_invest = (
            needed_amount if needed_amount < available_amount
            else available_amount)

        available_amount -= to_invest
        obj_for_invest.invested_amount += to_invest
        object_in.invested_amount += to_invest

        if obj_for_invest.full_amount == obj_for_invest.invested_amount:
            await close_invested_object(obj_for_invest)

        if not available_amount:
            await close_invested_object(object_in)
            break
    await session.commit()
    await session.refresh(object_in)
    return object_in

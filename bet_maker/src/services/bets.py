from decimal import Decimal
from uuid import UUID
from sqlalchemy import select, update
from config.enums import BetStateEnum
from db.database import async_session_factory
from db.models.bets import Bets
from services.base import BaseService


class BetsService(BaseService):
    @staticmethod
    async def list():
        async with async_session_factory() as session:
            query = select(Bets) 
            result = await session.execute(query)
            scalars = result.scalars().all()
            return [bet for bet in scalars]
           
    async def create(self,
                     event_id: UUID,
                     bet_amount: Decimal):
        async with async_session_factory() as session:
            bet = Bets(id=self.generate_id(), event_id=event_id, bet_amount=bet_amount, state=BetStateEnum.NEW)
            session.add(bet)
            await session.commit()
            return bet
        
    @staticmethod
    async def update(
                    event_id: UUID,
                     state: BetStateEnum
                    ):
        async with async_session_factory() as session:
            query = (
                update(Bets)
                .where(Bets.event_id == event_id)
                .values(
                    state=state
                )
            )
            await session.execute(query)
            await session.commit()
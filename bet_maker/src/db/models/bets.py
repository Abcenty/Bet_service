from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (
    Uuid,
    Numeric,
    Enum
)
from decimal import Decimal
from config.enums import BetStateEnum
from db.models.base import Base
from uuid import UUID


class Bets(Base):
    __tablename__ = "bets"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    event_id: Mapped[UUID] = mapped_column(Uuid, nullable=False)
    bet_amount: Mapped[Decimal] = mapped_column(Numeric(precision=8, scale=2), nullable=False)
    state: Mapped[BetStateEnum] = mapped_column(
        Enum(BetStateEnum),
        nullable=False,
    )
    
    def str(self):
        return f"Bet #{self.id}"
from decimal import Decimal
from typing import List
from uuid import UUID
from pydantic import BaseModel, Field

from config.enums import BetStateEnum


class CreateBetRequest(BaseModel):
    bet_amount: Decimal = Field(gt=0, repr=False)
    
    
class BetDTO(BaseModel):
    id: UUID
    event_id: UUID
    bet_amount: Decimal = Field(gt=0, repr=False)
    state: BetStateEnum
    
    
class GetBetsRequest(BaseModel):
    bets: List[BetDTO]
    
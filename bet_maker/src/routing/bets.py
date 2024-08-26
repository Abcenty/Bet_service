from typing import Annotated, List
from uuid import UUID
from fastapi import APIRouter, Depends, status

from routing.events import get_events
from schemas.bets import BetDTO, CreateBetRequest
from schemas.events import EventDTO
from services.bets import BetsService



bets_router = APIRouter()


@bets_router.post('/create_bet',
          status_code=status.HTTP_201_CREATED,
          )
async def create_bet(
    event_id: UUID,
    bet_service: Annotated[BetsService, Depends()],
    bet_input: CreateBetRequest,
):
    awailable_events = await get_events()
    validated_events = [EventDTO(**e) for e in awailable_events]
    
    count: int = 0
    for e in validated_events:
        if event_id == e.event_id:
            count = 1
            break
    if count == 0:
        raise
    
    bet = await bet_service.create(
        event_id=event_id,
        bet_amount=bet_input.bet_amount,
    )
    return bet


@bets_router.get('/get_bets',
         status_code=status.HTTP_200_OK)
async def get_bets(
    bet_service: Annotated[BetsService, Depends()],
) -> List[BetDTO]:
    response = await bet_service.list()
    return response
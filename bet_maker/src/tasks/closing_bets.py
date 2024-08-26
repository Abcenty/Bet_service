import asyncio
from routing.events import get_finished_events
from schemas.events import EventDTO
from config.enums import EventStateEnum, BetStateEnum
from services.bets import BetsService

async def closing_bets():
    while True:
        events = await get_finished_events()
        validated_events = [EventDTO(**e) for e in events]
        
        
        for e in validated_events:
            if e.state == EventStateEnum.FINISHED_WIN:
                await BetsService.update(event_id=e.event_id, state=BetStateEnum.FINISHED_WIN)
            else:
                await BetsService.update(event_id=e.event_id, state=BetStateEnum.FINISHED_LOSE)
        await asyncio.sleep(5)
        print('Закрываю ставки')
import time

from fastapi import APIRouter, HTTPException
from data.events import events
from schemas.events import Event

events_router = APIRouter()


@events_router.put('/event')
async def create_event(event: Event):
    if event.event_id not in events:
        events[event.event_id] = event
        return {}

    for p_name, p_value in event.model_dump(exclude_unset=True).items():
        setattr(events[event.event_id], p_name, p_value)

    return {}


@events_router.get('/event/{event_id}')
async def get_event(event_id: str):
    if event_id in events:
        return events[event_id]

    raise HTTPException(status_code=404, detail="Event not found")


@events_router.get('/events')
async def get_events():
    return list(e.model_dump() for e in events.values() if time.time() < e.deadline)


# @events_router.get('/finished_events')
# async def get_finished_events():
#     return list(e.model_dump() for e in events.values() if e.state == EventStateEnum.FINISHED_WIN or e.state == EventStateEnum.FINISHED_LOSE) 

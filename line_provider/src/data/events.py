import time
from schemas.events import Event
from config.enums import EventStateEnum


events: dict[str, Event] = {
    'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11': Event(event_id='a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', coefficient=1.2, deadline=int(time.time()) + 30, state=EventStateEnum.NEW),
    'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a12': Event(event_id='a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a12', coefficient=1.15, deadline=int(time.time()) + 1, state=EventStateEnum.NEW),
    'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a13': Event(event_id='a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a13', coefficient=1.67, deadline=int(time.time()) + 5, state=EventStateEnum.NEW)
}
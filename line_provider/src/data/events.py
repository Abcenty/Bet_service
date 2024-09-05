import time
from schemas.events import Event
from config.enums import EventStateEnum


events: dict[int, Event] = {
    1: Event(event_id=1, coefficient=1.2, deadline=int(time.time()) + 30, state=EventStateEnum.NEW),
    2: Event(event_id=2, coefficient=1.15, deadline=int(time.time()) + 1, state=EventStateEnum.NEW),
    3: Event(event_id=3, coefficient=1.67, deadline=int(time.time()) + 5, state=EventStateEnum.NEW)
}
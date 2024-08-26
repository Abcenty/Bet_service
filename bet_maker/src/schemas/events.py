from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel

from config.enums import EventStateEnum


class EventDTO(BaseModel):
    event_id: UUID
    coefficient: Decimal | None = None
    deadline: int | None = None
    state: EventStateEnum
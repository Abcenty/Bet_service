from decimal import Decimal
from typing import Optional
from uuid import UUID
from pydantic import BaseModel

from config.enums import EventStateEnum


class Event(BaseModel):
    event_id: UUID
    coefficient: Optional[Decimal] = None
    deadline: Optional[int] = None
    state: Optional[EventStateEnum] = None
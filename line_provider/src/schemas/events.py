from decimal import Decimal
from typing import Optional
from uuid import UUID
from pydantic import BaseModel

from config.enums import EventStateEnum


class Event(BaseModel):
    event_id: int
    coefficient: Optional[float] = None
    deadline: Optional[int] = None
    state: Optional[EventStateEnum] = None
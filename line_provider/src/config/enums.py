from enum import Enum

class EventStateEnum(str, Enum):
    NEW: str = 'NEW'
    FINISHED_WIN: str = 'FINISHED_WIN'
    FINISHED_LOSE: str = 'FINISHED_LOSE'
    DONE: str = "DONE"
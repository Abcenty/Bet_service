import enum

class EventStateEnum(enum.Enum):
    NEW = 'NEW'
    FINISHED_WIN = 'FINISHED_WIN'
    FINISHED_LOSE = 'FINISHED_LOSE'
    DONE = "DONE"
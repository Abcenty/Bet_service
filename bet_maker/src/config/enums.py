import enum

class BetStateEnum(enum.Enum):
    NEW = 'NEW'
    FINISHED_WIN = 'FINISHED_WIN'
    FINISHED_LOSE = 'FINISHED_LOSE'
    
    
class EventStateEnum(enum.Enum):
    NEW = 'NEW'
    FINISHED_WIN = 'FINISHED_WIN'
    FINISHED_LOSE = 'FINISHED_LOSE'
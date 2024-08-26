import asyncio
import time
from config.enums import EventStateEnum
from data.events import events

async def processing_events():
    while True:
        if time.time() % 2 >= 1:
            for e in events.values():
                if time.time() >= e.deadline and e.state == EventStateEnum.NEW:
                    e.state = EventStateEnum.FINISHED_WIN
        if time.time() % 2 < 1:
            for e in events.values():
                if time.time() >= e.deadline and e.state == EventStateEnum.NEW:
                    e.state = EventStateEnum.FINISHED_LOSE
        await asyncio.sleep(5)
        print('Обрабатываю ивенты')
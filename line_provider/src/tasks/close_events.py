import asyncio
import time
from config.enums import EventStateEnum
from data.events import events

async def close_events():
    while True:
        for e in events.values():
            if time.time() - 15 >= e.deadline:
                e.state = EventStateEnum.DONE
        await asyncio.sleep(15)
        print('Закрываю ивенты')
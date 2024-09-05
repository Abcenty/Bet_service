import asyncio
import uvicorn
from tasks.processing_events import processing_events
from tasks.close_events import close_events
from config.config import settings
from app import app
from rmq_server.publisher import set_task


@app.on_event('startup')
async def start():
    task_1 = asyncio.create_task(set_task()) # noqa
    task_1 = asyncio.create_task(processing_events()) # noqa
    task_2 = asyncio.create_task(close_events()) # noqa


# async def main():
#     task = asyncio.create_task(set_task())
#     await asyncio.gather(task)
    
        

if __name__ == "__main__":
    uvicorn.run("app:app",
        workers=settings().WORKERS_COUNT,
        host=settings().HOST,
        port=settings().PORT,
        log_level="info"
        )
    # asyncio.run(main())
    
    

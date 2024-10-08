import asyncio
import uvicorn
from rmq_client.consumer import consume
from tasks.closing_bets import closing_bets
from config.config import settings
from app import app


# @app.on_event('startup')
# async def start():
#     task_1 = asyncio.create_task(consume()) # noqa


# async def main():
#     task_1 = asyncio.create_task(consume()) # noqa
#     await asyncio.gather(task_1)

        

if __name__ == "__main__":
    uvicorn.run("app:app",
        workers=settings().WORKERS_COUNT,
        host=settings().HOST,
        port=settings().PORT,
        log_level="info"
        )
    # asyncio.run(main())
    










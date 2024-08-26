import asyncio
import uvicorn
from tasks.closing_bets import closing_bets
from config.config import settings
from app import app




    
@app.on_event('startup')
async def start():
    task_1 = asyncio.create_task(closing_bets()) # noqa
        

if __name__ == "__main__":
    uvicorn.run("app:app",
        workers=settings().WORKERS_COUNT,
        host=settings().HOST,
        port=settings().PORT,
        log_level="info"
        )
    










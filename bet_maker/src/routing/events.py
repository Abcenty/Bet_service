from typing import List
from fastapi import APIRouter
from config.config import settings

import aiohttp


events_router = APIRouter()

@events_router.get('/get_events')
async def get_events():
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get(f'http://{settings().PROVIDER_HOST}:{settings().PROVIDER_PORT}/events') as resp:
            response: List[dict] = await resp.json()
            return response
        
        
@events_router.get('/get_finished_events')
async def get_finished_events():
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get(f'http://{settings().PROVIDER_HOST}:{settings().PROVIDER_PORT}/finished_events') as resp:
            response: List[dict] = await resp.json()
            return response
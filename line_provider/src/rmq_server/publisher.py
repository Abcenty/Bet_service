import asyncio

import json
from aio_pika import Message, connect
from aiormq import AMQPConnectionError
from routing.events import get_events

from config.config import settings


async def set_task() -> None:
    retries = 10
        # Perform connection
    AMQP_USER = settings().AMQP_USER
    AMQP_PASS = settings().AMQP_PASS
    AMQP_HOST = settings().AMQP_HOST
    for attempt in range(retries):
        try:
            connection = await connect(f"amqp://{AMQP_USER}:{AMQP_PASS}@{AMQP_HOST}/")
            break
        except AMQPConnectionError:
            if attempt < retries - 1:
                await asyncio.sleep(2)  # Ждем перед следующей попыткой
            else:
                raise
    events = await get_events()
    async with connection:
        channel = await connection.channel()
        while True:
            await channel.default_exchange.publish(
                Message(body=json.dumps(events).encode()),
                routing_key='service_b_queue'
            )
            await asyncio.sleep(5)

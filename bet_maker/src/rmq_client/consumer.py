import asyncio
import json

from aio_pika import ExchangeType, connect
from aio_pika.abc import AbstractIncomingMessage

from config.config import settings


async def on_message(message: AbstractIncomingMessage) -> None:
    async with message.process():
        print(f"[x] {message.body}")


async def consume():
    # Perform connection
    AMQP_USER = settings().AMQP_USER
    AMQP_PASS = settings().AMQP_PASS
    AMQP_HOST = settings().AMQP_HOST

    
    connection = await connect(f"amqp://{AMQP_USER}:{AMQP_PASS}@{AMQP_HOST}/")

    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue('service_b_queue')

        async for message in queue:
            async with message.process():
                return json.loads(message.body)

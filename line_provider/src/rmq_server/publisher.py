import asyncio
import sys

from aio_pika import DeliveryMode, ExchangeType, Message, connect
from aiormq import AMQPConnectionError

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
            
    async with connection:
        channel = await connection.channel()

        logs_exchange = await channel.declare_exchange(
            "logs", ExchangeType.FANOUT,
        )

        message_body = b" ".join(
            arg.encode() for arg in sys.argv[1:]
        ) or b"Hello World!"

        message = Message(
            message_body,
            delivery_mode=DeliveryMode.PERSISTENT,
        )

        # Sending the message
        await logs_exchange.publish(message, routing_key="info")

        print(f" [x] Sent {message!r}")
        
        await asyncio.sleep(3)

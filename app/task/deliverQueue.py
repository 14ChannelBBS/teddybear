import asyncio
import aiohttp

dqueue = asyncio.Queue()

async def task():
    while True:
        if dqueue.qsize > 0:
            func = await dqueue.get()
            await func
import asyncio
import aiohttp
import logging

log = logging.getLogger("uvicorn")

dqueue = asyncio.Queue()
can = True

async def task():
    log.info("deliverQueue task started.")
    while can:
        if dqueue.qsize() > 0:
            func = await dqueue.get()
            await func
        await asyncio.sleep(1)
    return
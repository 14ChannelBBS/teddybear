import asyncio
import aiohttp
import logging
import traceback

log = logging.getLogger("uvicorn")

dqueue = asyncio.Queue()
can = True

async def task():
    log.info("deliverQueue task started.")
    while can:
        try:
            if dqueue.qsize() > 0:
                func = await dqueue.get()
                await func
        except Exception as e:
            traceback.print_exception(e)
        await asyncio.sleep(1)
    return
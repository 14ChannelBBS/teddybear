from fastapi import FastAPI
from app.api import registration
from app.wellknown import nodeinfo, webfinger
from app.activitypub import user, inbox
import logging
from app.config import Config
from app.task import deliverQueue, processQueue
import asyncio
from contextlib import asynccontextmanager
from concurrent.futures import Executor, ThreadPoolExecutor

log = logging.getLogger("uvicorn")
log.info(f"Teddybear v{Config.softwareVersion} is loading...")

@asynccontextmanager
async def lifespan(app: FastAPI):
    loop = asyncio.get_running_loop()
    pool = ThreadPoolExecutor(max_workers=20)
    future = loop.run_in_executor(pool, lambda: asyncio.run(deliverQueue.task()))
    future2 = loop.run_in_executor(pool, lambda: asyncio.run(processQueue.task()))
    yield
    deliverQueue.can = False
    processQueue.can = False
    pool.shutdown()
    return

app = FastAPI(lifespan=lifespan)

app.include_router(registration.router)
app.include_router(nodeinfo.router)
app.include_router(webfinger.router)
app.include_router(user.router)
app.include_router(inbox.router)

log.info(f"""Teddybear v{Config.softwareVersion} load successful!""")
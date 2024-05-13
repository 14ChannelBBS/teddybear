from fastapi import FastAPI
from app.api import registration
from app.wellknown import nodeinfo, webfinger
from app.activitypub import user, inbox
import logging
from app.config import Config

log = logging.getLogger("uvicorn")
log.info(f"Teddybear v{Config.softwareVersion} is loading...")

app = FastAPI()

app.include_router(registration.router)
app.include_router(nodeinfo.router)
app.include_router(webfinger.router)
app.include_router(user.router)
app.include_router(inbox.router)

log.info(f"""Teddybear v{Config.softwareVersion} load successful!""")
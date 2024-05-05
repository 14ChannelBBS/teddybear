from fastapi import FastAPI
from app.api import registration
from app.wellknown import nodeinfo, webfinger
from app.activitypub import user

app = FastAPI()

app.include_router(registration.router)
app.include_router(nodeinfo.router)
app.include_router(webfinger.router)
app.include_router(user.router)
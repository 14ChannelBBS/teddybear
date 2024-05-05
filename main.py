from fastapi import FastAPI
from app.api import registration
from app.wellknown import nodeinfo

app = FastAPI()

app.include_router(registration.router)
app.include_router(nodeinfo.router)

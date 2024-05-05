from fastapi import FastAPI
from app.api import registration

app = FastAPI()

app.include_router(registration.router)

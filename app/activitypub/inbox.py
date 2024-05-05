from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from ..config import Config
import asyncpg
import os

router = APIRouter()

@router.get("/inbox")
async def inbox(request: Request):
    if request.headers.get("Content-Type", "") != 'application/activity+json':
        raise HTTPException(status_code=400)

    data = await request.json()
    print(data)

    if type(data) != dict or 'type' not in data:
        return HTTPException(status=400)
    elif data['type'] == 'Follow':
        pass
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from ..config import Config
from ..task import processQueue
import asyncpg
import os

router = APIRouter()

@router.post("/users/{id}/inbox")
async def inbox(request: Request, id: str):
    if request.headers.get("Content-Type", "") != 'application/activity+json':
        raise HTTPException(status_code=400)

    data = await request.json()
    if type(data) != dict or 'type' not in data:
        return HTTPException(status=400)
    
    await processQueue.pqueue.put(
        (request.headers, data, f"/users/{id}/inbox", id)
    )
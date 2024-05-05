from fastapi import APIRouter, HTTPException
from ..config import Config
import asyncpg
import os
import re

router = APIRouter()

@router.get("/.well-known/webfinger")
async def webfinger(resource: str = ""):
    match = re.search(r"acct:(.*?)@(.*?)$", resource)

    if match:
        username = match.group(1)
        domain = match.group(2)

        if domain == Config.serverAddress:
            connection = await asyncpg.connect(os.getenv("dsn"))
            row = await connection.fetchrow('SELECT * FROM users WHERE username = $1', username)
            return {
                "subject": resource,
                "links": [
                    {
                        "rel": "self",
                        "type": "application/activity+json",
                        "href": f"https://{Config.serverAddress}/users/{row['id']}"
                    }
                ]
            }
        else:
            raise HTTPException(status_code=404)
    else:
        raise HTTPException(status_code=404)
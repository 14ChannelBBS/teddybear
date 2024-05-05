from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from ..config import Config
import asyncpg
import os

router = APIRouter()

@router.get("/users/{id}")
async def webfinger(id: str):
    connection = await asyncpg.connect(os.getenv("dsn"))
    row = await connection.fetchrow('SELECT * FROM users WHERE id = $1', id)

    body = {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://w3id.org/security/v1"
        ],
        "followers": f"https://{Config.serverAddress}/users/{row['id']}/followers",
        "following": f"https://{Config.serverAddress}/users/{row['id']}/following",
        "icon": {
            "type": "Image",
            "url": row["icon_url"]
        },
        "id": f"https://{Config.serverAddress}/users/{row['id']}",
        "inbox": f"https://{Config.serverAddress}/users/{row['id']}/inbox",
        "name": row['name'],
        "outbox": f"https://{Config.serverAddress}/users/{row['id']}/outbox",
        "preferredUsername": row['username'],
        "publicKey": {
            "id": f"https://{Config.serverAddress}/users/{row['id']}#main-key",
            "owner": f"https://{Config.serverAddress}/users/{row['id']}",
            "publicKeyPem": row['publicKeyPem'],
            "type": "Key"
        },
        "summary": row['summary'],
        "type": "Person",
        "url": f"https://{Config.serverAddress}/@{row['username']}"
    }
    return JSONResponse(body, headers={"Content-Type": "application/activity+json"})
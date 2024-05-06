from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from ..config import Config
import asyncpg
import os

router = APIRouter()

@router.post("/users/{id}/inbox")
async def inbox(request: Request, id: str):
    if request.headers.get("Content-Type", "") != 'application/activity+json':
        raise HTTPException(status_code=400)

    print(request.headers)
    data = await request.json()
    print(data)

    """
    フォローするとこんな感じのデータが返ってくるのでいい感じに処理する
    {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://w3id.org/security/v1",
            {
                "Key": "sec:Key",
                "manuallyApprovesFollowers": "as:manuallyApprovesFollowers",
                "sensitive": "as:sensitive",
                "Hashtag": "as:Hashtag",
                "quoteUrl": "as:quoteUrl",
                "toot": "http://joinmastodon.org/ns#",
                "Emoji": "toot:Emoji",
                "featured": "toot:featured",
                "discoverable": "toot:discoverable",
                "schema": "http://schema.org#",
                "PropertyValue": "schema:PropertyValue",
                "value": "schema:value",
                "misskey": "https://misskey-hub.net/ns#",
                "_misskey_content": "misskey:_misskey_content",
                "_misskey_quote": "misskey:_misskey_quote",
                "_misskey_reaction": "misskey:_misskey_reaction",
                "_misskey_votes": "misskey:_misskey_votes",
                "_misskey_summary": "misskey:_misskey_summary",
                "isCat": "misskey:isCat",
                "vcard": "http://www.w3.org/2006/vcard/ns#"
            }
        ],
        "id": "https://misskey.nukumori-sky.net/follows/9swzzfvm9v",
        "type": "Follow",
        "actor": "https://misskey.nukumori-sky.net/users/9nzv0t51qm",
        "object": "https://beta.14chan.jp/users/Cyr2LWeSCM"
    }
    """

    if type(data) != dict or 'type' not in data:
        return HTTPException(status=400)
    elif data['type'] == 'Follow':
        connection = await asyncpg.connect(os.getenv("dsn"))
        json = await connection.fetchval('SELECT followers FROM users WHERE id = $1', id)
        json.append()
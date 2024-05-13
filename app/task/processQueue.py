import asyncio
import aiohttp
from ..utils import verify_signature, sign_headers
import asyncpg
import os
from . import deliverQueue
from ..config import Config
import logging
import base64

log = logging.getLogger("uvicorn")
pqueue = asyncio.Queue()
can = True

async def task():
    log.info("processQueue task started.")
    while can:
        if pqueue.qsize() > 0:
            header, body, path, id = await pqueue.get()

            if body.get("type", "") == "Follow":
                await followTask(header, body, path, id)
        await asyncio.sleep(1)
    return

async def followTask(header, body, path, id):
    headers = {
        'Accept': 'application/activity+json'  # Acceptヘッダーを設定
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(body.get("actor"), headers=headers) as response:
            if response.status == 200:
                userdata = await response.json()
            else:
                Exception("This fediverse user not found")

    if userdata["publicKey"]["owner"] == body.get("actor"):
        if userdata["publicKey"]["type"] == "Key":
            public_key_str = userdata["publicKey"]["publicKeyPem"]
            public_key_bytes = base64.b64decode(public_key_str.encode())
            public_key = bytearray(public_key_bytes)
        else:
            Exception("publicKey type is not Key")
    else:
        Exception("publicKey error")

    if verify_signature(header['signature'], "POST", path, header, public_key):
        connection = await asyncpg.connect(os.getenv("dsn"))
        mydata = await connection.fetchrow('SELECT * FROM users WHERE id = $1', id)
        mydata["followers"].append(body.get("actor"))
        await connection.execute('''
            UPDATE users
            SET followers = $2
            WHERE id = $1
        ''', id, mydata["followers"])
        await connection.close()

        await deliverQueue.dqueue.put(
            follow_accept(header, body, path, id, userdata, mydata)
        )
    else:
        Exception("signature verify error")

async def follow_accept(header, body, path, id, userdata, mydata):
    headers = sign_headers(mydata, "POST", f"/u/{id}")
    headers["Content-Type"] = "application/activity+json"
    data = {
        '@context': 'https://www.w3.org/ns/activitystreams',
        'type': 'Accept',
        'actor': f"https://{Config.serverAddress}/u/{id}", # フォローを受け付けるアカウントのPersonのid
        'object': body,
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(body.get("actor"), headers=headers, json=data) as response:
            if response.code >= 400 and response.code < 600:
                log.error("follow accept error...")
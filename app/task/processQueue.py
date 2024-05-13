import asyncio
import aiohttp
from ..utils import verify_signature, sign_headers
import asyncpg
import os
from . import deliverQueue
from ..config import Config
import logging
import base64
import traceback
import rsa

log = logging.getLogger("uvicorn")
pqueue = asyncio.Queue()
can = True

async def task():
    log.info("processQueue task started.")
    while can:
        try:
            if pqueue.qsize() > 0:
                header, body, path, id = await pqueue.get()

                if body.get("type", "") == "Follow":
                    await followTask(header, body, path, id)
        except Exception as e:
            traceback.print_exception(e)
        await asyncio.sleep(0.01)
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
            pubBytes = bytes(public_key_str.encode("UTF-8"))
            n = int.from_bytes(pubBytes[8:8+128], 'big')
            e = int.from_bytes(pubBytes[8+128:], 'big')
            pubKey = rsa.PublicKey(**{'e': e, 'n': n})
            public_key = pubKey.save_pkcs1().decode()
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

        log.info(f'{body.get("actor")} followed {mydata["username"]}.')

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
            else:
                log.info(f'accepted!')
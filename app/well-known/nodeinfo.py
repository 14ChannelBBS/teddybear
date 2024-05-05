from fastapi import APIRouter

router = APIRouter()

@router.get("/.well-known/nodeinfo")
async def nodeinfo():
    return {
        "links": [
            {
            "rel": "http://nodeinfo.diaspora.software/ns/schema/2.1",
            "href": "https://misskey.io/nodeinfo/2.1"
            },
            {
            "rel": "http://nodeinfo.diaspora.software/ns/schema/2.0",
            "href": "https://misskey.io/nodeinfo/2.0"
            }
        ]
    }
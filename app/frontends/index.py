from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def inbox(request: Request):
    return "Teddybear Public beta<br>\n現在登録は受け付けていません。\nContact Us: nennneko5787 (at) 14chan (dot) jp"
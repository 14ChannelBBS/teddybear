from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def inbox(request: Request):
    return """
    <h1>Teddybear Public beta</h1>
    <b>現在登録は受け付けていません。</b><small>そのうち完成させるつもりです...</small><br>
    Github Repository: <a href="https://github.com/14ChannelBBS/teddybear">https://github.com/14ChannelBBS/teddybear</a><br>
    Contact Us: nennneko5787 (at) 14chan (dot) jp
    """
from fastapi import APIRouter
from validate_email import validate_email

router = APIRouter()

@router.get("/registration/emailcheck")
async def emailcheck(address: str = ""):
    if validate_email(address):
        return {"valid": True}
    else:
        return {"valid": False}


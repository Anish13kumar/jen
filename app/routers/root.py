from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
def root():
    return JSONResponse(content={"message":"Home_Page"},status_code=200)
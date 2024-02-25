from fastapi import FastAPI
from app.routers import root
import uvicorn


app = FastAPI()

app.include_router(root.router , tags=["Root"])


if __name__ == "__main__":
    uvicorn.run("run:app",host="0.0.0.0",port=8090,reload=True)
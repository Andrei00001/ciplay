from fastapi import FastAPI

from app.statistics.router import router as router_statistics
app = FastAPI()

app.include_router(
    router_statistics
)

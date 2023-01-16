from fastapi import FastAPI

from app.statistics.router import router as router_url
app = FastAPI()

app.include_router(
    router_url
)

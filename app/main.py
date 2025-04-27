from fastapi import FastAPI
from .config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/config")
async def get_config():
    return {
        "app_name": settings.APP_NAME,
        "app_version": settings.APP_VERSION,
        "database_url": settings.DATABASE_URL,
        "debug": settings.DEBUG
    }
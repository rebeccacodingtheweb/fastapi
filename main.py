import fastapi
import uvicorn
import os

from dotenv import load_dotenv
from starlette.staticfiles import StaticFiles

from api import weather_api
from services import openweather_service
from views import home

api = fastapi.FastAPI()


def configure():
    configure_routing()
    configure_apikeys()


def configure_routing():
    api.mount("/static", StaticFiles(directory="static"), name="static")
    api.include_router(home.router)
    api.include_router(weather_api.router)


def configure_apikeys():
    load_dotenv()
    openweather_service.api_key = os.getenv("API_KEY")


if __name__ == "__main__":
    configure()
    uvicorn.run(api)

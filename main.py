import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get("/")
def index():
    return "Hello Weather App"


if __name__ == "__main__":
    uvicorn.run(api)

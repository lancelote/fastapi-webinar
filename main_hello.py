import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get('/')
def index():
    return {
        "message": "hello world",
        "status": "OK",
    }


uvicorn.run(api, host="127.0.0.1", port=8000)

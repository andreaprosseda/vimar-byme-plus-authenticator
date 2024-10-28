from fastapi import FastAPI
import uvicorn
from src.config.api_config import initialize
from src.config.startup_config import on_startup
from src.util.envs import PORT

app = FastAPI(on_startup=[on_startup])
initialize(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=PORT, reload=True)
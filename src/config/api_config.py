from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ..api.all import define_routers
from ..util.envs import APP_NAME, VERSION

def initialize(app: FastAPI):
    app.title = APP_NAME
    app.version = VERSION
    add_middleware(app)
    define_routers(app)
    
    
def add_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True
    )
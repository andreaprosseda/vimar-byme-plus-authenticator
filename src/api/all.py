from fastapi import FastAPI, APIRouter
from .vimar_api import router as VimarRouter
from .common_api import router as CommonRouter
from .probe_api import router as ProbeRouter

def define_routers(app: FastAPI):
    app.include_router(router_api())
    app.include_router(router_common())
        

def router_common() -> APIRouter:
    router = APIRouter()
    router.include_router(CommonRouter)
    router.include_router(ProbeRouter)
    return router


def router_api() -> APIRouter:
    router = APIRouter(prefix="/api")
    router.include_router(VimarRouter)
    return router
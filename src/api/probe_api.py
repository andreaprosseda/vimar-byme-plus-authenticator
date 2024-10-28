from fastapi import APIRouter
from ..controller.probe_ctl import ProbeController


router = APIRouter(tags=["Probes"])
controller = ProbeController()


@router.get("/health")
async def health():
    return await controller.health()


@router.get("/ready")
async def ready():
    return await controller.ready()
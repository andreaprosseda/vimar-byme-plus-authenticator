from fastapi import APIRouter

from ..model.association_request import AssociationRequest
from ..model.operational_request import OperationalRequest
from ..model.credential_response import CredentialResponse
from ..model.identifier_response import IdentifierResponse
from ..controller.vimar_ctl import VimarController

router = APIRouter(prefix="/vimar", tags=["Vimar"])
controller = VimarController()


@router.get("/identifier", response_model=IdentifierResponse)
async def get_identifier():
    return await controller.get_identifier()


@router.post("/phases/association/credentials", response_model=CredentialResponse)
async def get_association_credentials(association_request: AssociationRequest):
    return await controller.get_association_credentials(association_request)


@router.post("/phases/operational/credentials", response_model=CredentialResponse)
async def get_operational_credentials(operational_request: OperationalRequest):
    return await controller.get_operational_credentials(operational_request)
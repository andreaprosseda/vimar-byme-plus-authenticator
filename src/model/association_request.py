from pydantic import BaseModel

class AssociationRequest(BaseModel):
    username: str | None = None
    setup_code: str | None = None
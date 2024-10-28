from pydantic import BaseModel

class IdentifierResponse(BaseModel):
    username: str
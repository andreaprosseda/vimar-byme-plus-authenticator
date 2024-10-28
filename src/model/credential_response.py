from pydantic import BaseModel

class CredentialResponse(BaseModel):
    username: str
    userid: str
    password: str
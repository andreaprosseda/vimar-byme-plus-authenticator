from pydantic import BaseModel

class OperationalRequest(BaseModel):
    username: str | None = None
    userid: str | None = None
    password: str | None = None
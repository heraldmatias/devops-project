from pydantic import BaseModel


class LoginBody(BaseModel):
    application: str


class LoginResponse(BaseModel):
    token: str

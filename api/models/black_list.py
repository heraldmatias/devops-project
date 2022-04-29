from datetime import datetime
from pydantic import BaseModel


class BlackEmailBody(BaseModel):
    app_id: str
    email: str
    blocked_reason: str


class BlackEmailResponse(BaseModel):
    email: str
    created_ts: datetime
    app_id: str
    blocked_reason: str
    id: int
    ip_address: str

from pydantic import BaseModel

class Driver(BaseModel):
    email: str
    phone: str
    current_location: str
    available: bool
    documents_verified: bool
    account_suspended: bool
    acceptance_rate: float
    response_time: float
from pydantic import BaseModel
from datetime import datetime

class SystemAlert(BaseModel):
    type: str
    severity: str
    message: str
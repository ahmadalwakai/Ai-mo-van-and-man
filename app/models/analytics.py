from pydantic import BaseModel
from datetime import datetime

class SystemMetric(BaseModel):
    timestamp: datetime
    response_time: float
    cpu_usage: float
    memory_usage: float
    error_rate: float
    active_users: int
    pending_orders: int
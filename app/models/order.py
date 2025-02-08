from pydantic import BaseModel
from datetime import datetime

class Order(BaseModel):
    user_id: int
    origin: str
    destination: str
    price: float
    floor_origin: int
    elevator_origin: bool
    floor_dest: int
    elevator_dest: bool
    scheduled_time: datetime
    special_instructions: str
    weather_conditions: dict
    traffic_conditions: dict
    multi_stop: bool
    family_account: bool
    insurance_required: bool
    insurance_cost: float
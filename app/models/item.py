from pydantic import BaseModel

class Item(BaseModel):
    name: str
    weight: float
    volume: float
    category: str
    image_url: str
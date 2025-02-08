from app.models.pricing import PricingModel

class PricingService:
    def __init__(self):
        self.pricing_model = PricingModel()

    async def calculate_price(self, order_data: dict):
        return await self.pricing_model.predict_price(order_data)
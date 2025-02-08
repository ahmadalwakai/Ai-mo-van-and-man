import aioredis
import json
from datetime import datetime
from app.models.order import Order

class TrackingService:
    def __init__(self):
        self.redis = aioredis.from_url("redis://localhost")

    async def update_location(self, order_id, driver_location):
        if not driver_location or len(driver_location.split(',')) != 2:
            raise ValueError("Invalid driver location format")
        
        tracking_key = f"order_tracking:{order_id}"
        tracking_data = {
            'location': driver_location,
            'timestamp': datetime.utcnow().isoformat(),
            'status': 'active'
        }
        await self.redis.set(tracking_key, json.dumps(tracking_data), expire=3600)

    async def get_location(self, order_id):
        tracking_key = f"order_tracking:{order_id}"
        tracking_data = await self.redis.get(tracking_key)
        if tracking_data:
            return json.loads(tracking_data)
        return None

    async def calculate_eta(self, order_id):
        order = await Order.filter(id=order_id).first()
        tracking_data = await self.get_location(order_id)

        if order and tracking_data:
            current_location = tracking_data['location']
            destination = order.destination

            directions = await asyncio.to_thread(gmaps.directions, current_location, destination, mode="driving", departure_time=tracking_data['timestamp'])

            if directions and directions[0]['legs'][0].get('duration_in_traffic'):
                duration_seconds = directions[0]['legs'][0]['duration_in_traffic']['value']
                eta = datetime.utcnow() + timedelta(seconds=duration_seconds)
                return eta

        return None

    async def close(self):
        await self.redis.close()
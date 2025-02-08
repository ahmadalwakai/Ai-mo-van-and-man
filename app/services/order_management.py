from fastapi import HTTPException, status
from datetime import datetime
from app.models.order import Order

class OrderManagementService:
    async def create_order(self, order_data: dict):
        order = Order(**order_data)
        await order.save()
        return order

    async def update_order_status(self, order_id: int, status: str, reason: str = None):
        order = await Order.filter(id=order_id).first()
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")

        order.status = status
        if status == 'completed':
            order.completed_at = datetime.utcnow()
        elif status == 'cancelled':
            order.cancellation_reason = reason

        await order.save()
        return order
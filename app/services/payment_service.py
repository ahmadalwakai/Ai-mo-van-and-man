import os
import stripe
from fastapi import HTTPException, status

class PaymentService:
    def __init__(self):
        stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
        if not stripe.api_key:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Stripe secret key not found")

    def create_payment_intent(self, amount: int, currency: str = 'usd'):
        try:
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency=currency
            )
            return intent
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
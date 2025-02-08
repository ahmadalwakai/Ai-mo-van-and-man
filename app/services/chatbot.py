import os
import asyncio
import logging
from google.cloud import dialogflow_v2
from app.models.pricing import PricingModel

class ChatbotAssistant:
    def __init__(self):
        self.dialogflow_client = dialogflow_v2.SessionsClient()

    async def handle_booking_request(self, user_id, message):
        try:
            session = self.dialogflow_client.session_path(os.getenv('DIALOGFLOW_PROJECT_ID'), user_id)
            response = await asyncio.to_thread(self.dialogflow_client.detect_intent, session=session, query_input={"text": {"text": message, "language_code": "en"}})

            intent = response.query_result.intent.display_name
            parameters = dict(response.query_result.parameters)

            if intent == "book_move":
                order_data = {
                    'origin': parameters.get('origin-location', ''),
                    'destination': parameters.get('destination-location', ''),
                    'items': [
                        {'name': 'Couch', 'weight': 50, 'volume': 20, 'category': 'furniture'},
                        {'name': 'TV', 'weight': 15, 'volume': 5, 'category': 'electronics'}
                    ],
                    'floor_origin': parameters.get('floor-origin', 0),
                    'elevator_origin': parameters.get('elevator-origin', False),
                    'floor_dest': parameters.get('floor-destination', 0),
                    'elevator_dest': parameters.get('elevator-destination', False),
                    'scheduled_time': parameters.get('date-time', '')
                }

                pricing_model = PricingModel()
                price_details = await pricing_model.predict_price(order_data)

                return {
                    'order_data
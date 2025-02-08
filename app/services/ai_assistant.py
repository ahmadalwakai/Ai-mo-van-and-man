import os
import openai

class AIAssistantService:
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')

    async def generate_item_image(self, item_type, size):
        try:
            prompt = f"Generate a realistic and detailed image of a {item_type} in size {size}"
            response = await openai.Image.create(prompt=prompt, n=1, size="512x512")
            return response['data'][0]['url']
        except Exception as e:
            logging.error(f"Error generating image: {e}")
            return None
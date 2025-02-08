async def send_push_notification(token, title, message, data=None):
    if not token:
        raise ValueError("Invalid FCM token")
    # Implementation for sending push notification
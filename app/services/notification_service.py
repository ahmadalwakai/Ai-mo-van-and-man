import os
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

class NotificationService:
    async def send_email(self, to, subject, body, attachments=None):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = os.getenv('MAIL_USERNAME')
        msg['To'] = to

        if attachments:
            for attachment in attachments:
                part = MIMEApplication(attachment['data'])
                part.add_header('Content-Disposition', 'attachment', filename=attachment['name'])
                msg.attach(part)

        smtp_host = os.getenv('SMTP_HOST', 'localhost')
        smtp_port = os.getenv('SMTP_PORT', 465)
        smtp_user = os.getenv('SMTP_USER')
        smtp_pass = os.getenv('SMTP_PASS')

        server = smtplib.SMTP_SSL(smtp_host, smtp_port)
        server.login(smtp_user, smtp_pass)
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
        server.quit()

    async def send_push_notification(self, token, title, message, data=None):
        if not token:
            raise ValueError("Invalid FCM token")
        # Implementation for sending push notification
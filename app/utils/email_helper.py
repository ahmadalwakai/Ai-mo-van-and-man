import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

async def send_email(to, subject, body, attachments=None):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = os.getenv('MAIL_USERNAME')
    msg['To'] = to

    if attachments:
        for attachment in attachments:
            part = MIMEApplication(attachment['data'])
            part.add_header('Content-Disposition', 'attachment', filename=attachment['name'])
            msg.attach(part)

    smtp_host = os.getenv('SMTP_HOST')
    smtp_port = int(os.getenv('SMTP_PORT'))
    smtp_user = os.getenv('SMTP_USER')
    smtp_pass = os.getenv('SMTP_PASS')

    server = smtplib.SMTP_SSL(smtp_host, smtp_port)
    server.login(smtp_user, smtp_pass)
    server.sendmail(msg['From'], [msg['To']], msg.as_string())
    server.quit()
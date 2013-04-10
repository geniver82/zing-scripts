from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os.path
import settings
import smtplib

PASSWORD = settings.PASSWORD
SENDER = settings.SENDER
RECIPIENT = settings.RECIPIENT
POSITION_APPLIED = settings.POSITION_APPLIED
SUBJECT = settings.SUBJECT
BODY = settings.BODY
CV_LOCATION = settings.CV_LOCATION

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def run():
    msg = get_attachment_and_body()
    send_email(msg)

def send_email(content):
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

    # identify ourself to an ESMTP server using EHLO
    session.ehlo()

    # put the SMTP connection in TLS (Transport Layer Security) mode
    session.starttls()

    session.ehlo

    # login with credentials. all transactions are encrypted.
    session.login(SENDER, PASSWORD)
    session.sendmail(SENDER, RECIPIENT, content)
    session.quit()

def get_attachment_and_body():
    msg = MIMEMultipart()

    # Set subject, sender and recipient
    msg['Subject'] = SUBJECT
    msg['Sender'] = SENDER
    msg['To'] = RECIPIENT

    # Set resume attachment
    attachment = MIMEApplication(open(CV_LOCATION, 'rb').read())
    filename = os.path.basename(CV_LOCATION)
    attachment.add_header('Content-Disposition', 'attachment', 
        filename =filename)
    msg.attach(attachment)

    # Set HTML email body
    body = MIMEText(BODY, 'html')
    msg.attach(body)
    return msg.as_string()

def get_headers_for_plaintext():
    headers = [
    'From: ' + SENDER,
    'Subject: ' + SUBJECT,
    'To: ' + RECIPIENT,
    'MIME-Version: 1.0',
    'Content-Type: text/html']
    return '\r\n'.join(headers)

run()
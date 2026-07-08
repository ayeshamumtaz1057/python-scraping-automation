"""
mailer.py
---------
Sends the generated report as an email attachment using Gmail SMTP.

IMPORTANT SETUP (Gmail):
1. Apne Google account par 2-Step Verification on karein.
2. https://myaccount.google.com/apppasswords par jaa kar ek "App Password" banayein.
3. Wo 16-character app password config.py mein use karein (normal Gmail password NAHI).
"""

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_email_with_attachment(sender_email, sender_password, receiver_email,
                                 subject, body, attachment_path):
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, "rb") as f:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(attachment_path)}"
        )
        msg.attach(part)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)

    print(f"Email sent to {receiver_email}")

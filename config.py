"""
config.py
---------
Apni email details yahan daalein.
Behtar tareeqa: environment variables use karein taake password code mein na dikhe.
"""

import os

SENDER_EMAIL = os.getenv("SENDER_EMAIL", "your_email@gmail.com")
SENDER_APP_PASSWORD = os.getenv("SENDER_APP_PASSWORD", "your_16_char_app_password")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL", "receiver_email@gmail.com")

"""
config.py
---------
Apni email details yahan daalein.
Behtar tareeqa: environment variables use karein taake password code mein na dikhe.
"""

import os

SENDER_EMAIL = os.getenv("SENDER_EMAIL", "ayeshamumtaz1057@gmail.com")
SENDER_APP_PASSWORD = os.getenv("SENDER_APP_PASSWORD", "akrlnngytangppli")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL", "ayeshamumtaz1057@gmail.com")
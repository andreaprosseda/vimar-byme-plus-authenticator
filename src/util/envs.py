import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "Vimar Byme Plus Authenticator - Signed Credential Issuer"
VERSION = "v1.0.0"

USERNAME = os.getenv('USERNAME')
PEM_PATH = os.getenv('PEM_PATH')
PORT = os.getenv('PORT', 9100)
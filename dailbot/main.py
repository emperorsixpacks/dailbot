import os

from dotenv import load_dotenv
from fastapi import FastAPI
from twilio.rest import Client

from dailbot.settings import AppSettings

load_dotenv(".env")

app_settings = AppSettings()
app = FastAPI()

TWILIO_SSID = os.getenv("TWILIO_SSID", None)
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", None)
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER", None)

twilio_client = Client(TWILIO_SSID, TWILIO_AUTH_TOKEN)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, port=app_settings.port, host=app_settings.host)


# TODO write function to get env path

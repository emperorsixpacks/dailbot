import os
from hashlib import new

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from pyairtable.api import Api
from starlette import middleware
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from twilio.rest import Client
from twilio.rest.conversations.v1.configuration import webhook

from dailbot.settings import AirtableSettings, AppSettings, TailwindSettings
from dailbot.utils import create_new_webhook, read_webhook, write_webhook

load_dotenv(".env")

app_settings = AppSettings()
twilio_settings = TailwindSettings()
airtable_settings = AirtableSettings()

ORIGINS = ["127.0.0.1", "adapted-kindly-perch.ngrok-free.app"]
WEBHOOK_URL = f"{app_settings.public_url}/webhook"

airtable_api = Api(airtable_settings.airtable_access_token).base(
    airtable_settings.airtable_base_id
)

middlewares = [
    Middleware(
        CORSMiddleware,
        allow_origins=[ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        #        allow_headers=["*"],
    ),
]

new_webhook = create_new_webhook(airtable_api, WEBHOOK_URL)

if new_webhook is not None:
    write_webhook(new_webhook)

DEFAULT_WEBHOOK = read_webhook()


@app.post("/webhook", response_model=None)
async def airtable_notification(request: Request):
    await request.body()
    await request.headers
    return 200


TWILIO_SSID = os.getenv("TWILIO_SSID", None)
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", None)
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER", None)

twilio_client = Client(TWILIO_SSID, TWILIO_AUTH_TOKEN)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, port=app_settings.port, host=app_settings.host)


# TODO write function to get env path

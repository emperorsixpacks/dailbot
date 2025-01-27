import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from pyairtable.api import Api
from starlette import middleware
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from twilio.rest import Client

from dailbot.settings import AirtableSettings, AppSettings, TailwindSettings

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
"""
airtable_api.add_webhook(
    notify_url=WEBHOOK_URL,
    spec={
        "options": {
            "filters": {
                "dataTypes": ["tableData"],
                "recordChangeScope": "tblZbNhBmDblSUXR1",
            }
        }
    },
)
"""
app = FastAPI(middleware=middlewares)


@app.post("/webhook", response_model=None)
async def airtable_notification(request: Request):
    print(request)
    return 200


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, port=app_settings.port, host=app_settings.host)


# TODO write function to get env path

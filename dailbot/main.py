import os

from dotenv import load_dotenv
from fastapi import FastAPI
from twilio.rest import Client

from dailbot.settings import AirtableSettings, AppSettings, TailwindSettings

load_dotenv(".env")

app_settings = AppSettings()
app = FastAPI()

twilio_settings = TailwindSettings()
airtable_settings = AirtableSettings()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, port=app_settings.port, host=app_settings.host)


# TODO write function to get env path

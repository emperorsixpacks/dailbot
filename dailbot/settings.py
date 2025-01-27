from pydantic.fields import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from twilio.base.client_base import os

from dailbot.utils import BASE_DIR

env_dir = os.path.join(BASE_DIR, ".env")


class BaseConfig(BaseSettings):
    """
    Base class for settings to inherit from.

    This class loads environment variables from a .env file and ignores any
    extra variables that are not defined in the pydantic model.
    """

    model_config = SettingsConfigDict(
        env_file=(env_dir), env_file_encoding="utf-8", extra="ignore"
    )


class AppSettings(BaseConfig):
    debug: bool = Field(default=True)
    port: int = Field(default=5000)
    host: str = Field(default="localhost")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    public_url: str
=======
>>>>>>> 5997272 (feat: added settings)
=======
    public_url: str
>>>>>>> 8134ec3 (mod: added check in webhook creation)


class TailwindSettings(BaseConfig):
    twilio_ssid: str
    twilio_auth_token: str
    twilio_phone_number: str


class AirtableSettings(BaseConfig):
    airtable_access_token: str
<<<<<<< HEAD
<<<<<<< HEAD
    airtable_base_id: str
=======
>>>>>>> 9fbfc03 (feat: added tailwind and daisycss)
=======
>>>>>>> 5997272 (feat: added settings)
=======
    airtable_base_id: str
>>>>>>> 8134ec3 (mod: added check in webhook creation)

from pydantic.fields import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    """
    Base class for settings to inherit from.

    This class loads environment variables from a .env file and ignores any
    extra variables that are not defined in the pydantic model.
    """

    model_config = SettingsConfigDict(
        env_file=("../.env.prod", "../.env"), env_file_encoding="utf-8", extra="ignore"
    )


class AppSettings(BaseConfig):
    Debug: bool = Field(default=True)
    Port: int = Field(default=8000)
    Host: str = Field(default="127.0.0.1")

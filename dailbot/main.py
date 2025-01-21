from fastapi import FastAPI

from dailbot.settings import AppSettings

app_settings = AppSettings()
app = FastAPI()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, port=app_settings.Debug, host=app_settings.Host)

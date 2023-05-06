from pydantic import BaseSettings


class Settings(BaseSettings):
    env_test: str

    class Config:
        env_file = ".env"


settings = Settings()

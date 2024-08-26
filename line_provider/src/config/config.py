import functools

from dotenv import load_dotenv

from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    """Project settings."""

    WORKERS_COUNT: int
    HOST: str
    PORT: int

    
    model_config = SettingsConfigDict(env_file=".env")


@functools.lru_cache
def settings() -> Settings:
    return Settings()  # type: ignore
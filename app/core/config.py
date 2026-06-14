from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    APP_ENV: str = "local"

    OPENAI_API_KEY: str
    OPENAI_CHAT_MODEL: str

    OPENSEARCH_HOST: str
    OPENSEARCH_PORT: int = 9200
    OPENSEARCH_USE_SSL: bool = True
    OPENSEARCH_VERIFY_CERTS: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

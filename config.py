from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    gurobi_api_key: str = Field(..., description="Gurobi optimization API key")

    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)


settings = Settings()

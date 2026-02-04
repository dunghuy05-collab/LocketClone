from pydantic_settings import BaseSettings
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Locket Clone"
    database_url: str = ""
    secret_key:str = "CHANGE_ME"
    algorithm: str = "HS256"
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

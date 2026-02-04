from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Locket Clone"
    database_url: str = "sqlite:///./app.db"
    secret_key:str = "CHANGE_ME"
    algorithm: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()

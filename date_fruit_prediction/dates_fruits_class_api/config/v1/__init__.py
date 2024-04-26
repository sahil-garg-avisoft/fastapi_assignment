from pydantic_settings import BaseSettings

class BaseSettingsWrapper(BaseSettings):

    class Config:
        env_file = ".env"

#docker-compose -f .\dockerfiles\docker-compose.yml --env-file .\.env up --build
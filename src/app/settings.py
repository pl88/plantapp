from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///./plant.db'
    TEST_DATABASE_URI: str = 'sqlite:////tests/test.db'

settings = Settings()
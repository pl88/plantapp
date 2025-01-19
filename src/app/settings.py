from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///plant.db'
    SQLALCHEMY_TEST_DB_URI: str = 'sqlite:///test.db'


settings = Settings()
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: str = "postgresql+psycopg2://plant_admin:plant_password@db:5432/plantapp_db"
    TEST_DATABASE_URI: str = 'sqlite:////tests/test.db'


settings = Settings()

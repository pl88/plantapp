"""app settigs using pydantic
Example:

From pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SQLALCHEMy_DATABASE_URI: str = "plant.db"

    
settings = Settings()
"""
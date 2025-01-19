import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic import command
from alembic.config import Config
import os
from app.settings import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)




@pytest.fixture
def test_db():
    # alembic upgrade db
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option('sqlalchemy.url', settings.SQLALCHEMY_DATABASE_URI)
    command.upgrade(alembic_cfg, "head")

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        # os.remove(test_db_path)
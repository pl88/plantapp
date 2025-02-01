import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic.config import Config
from alembic import command

import os

from settings import settings

test_db_name = 'test.db'
test_db_path = f"sqlite:///{test_db_name}"
os.environ["SQLALCHEMY_DATABASE_URI"] = test_db_path
engine = create_engine(test_db_path, echo=True)
SessionLocal = sessionmaker(autoflush=False, bind=engine, autobegin=True)

@pytest.fixture
def test_db():
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", settings.SQLALCHEMY_DATABASE_URI)
    command.upgrade(alembic_cfg, "head")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        os.remove('test.db')

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os






@pytest.fixture
def test_db():
    test_db_path='test.db'
    engine = create_engine("sqlite:///"+test_db_path, echo=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        pass
        # db.close()
        # os.remove(test_db_path)
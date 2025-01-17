"""DB session file.
Should contain get_db() method for getting current db
Example:

from sqlalcem import create_engine
from sqlalchemy.orm import sessionmaker

from settings import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autobegin=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
"""


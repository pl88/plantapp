from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import Settings

engine = create_engine(Settings.SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

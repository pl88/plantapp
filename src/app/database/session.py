from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from settings import settints

engine = create_engine('sqlite:///dummy.db')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

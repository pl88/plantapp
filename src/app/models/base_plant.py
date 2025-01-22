from sqlalchemy import Integer, Column, String


class BasePlant:
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

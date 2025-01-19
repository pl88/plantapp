from .base import Base
from sqlalchemy import Column, Integer, String


class Plant(Base):
    __tablename__ = "plant"
    id = Column(Integer, primary_key=True)
    name = Column(String)


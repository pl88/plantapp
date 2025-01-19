from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String


class Plant(BaseModel):
    __tablename__ = "plant"
    id = Column(Integer, primary_key=True)
    name = Column(String)

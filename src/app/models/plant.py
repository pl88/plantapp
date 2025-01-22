from models.base import BaseModel
from models.base_plant import BasePlant


class Plant(BasePlant, BaseModel):
    __tablename__ = "plant"

"""This module should give us methods that perform actions on db common to BasePlant child models
Example:

from sqlalchemy.orm import Session

from database.session import get_db
from models.base_plant import BasePlant

class BasePlantRepository:
    db_session: Session
    model: BasePlant = BasePlant

    def __init__(self, db_session:Session = None) -> None:
        self.db_session = db_session or next(get_db())

    def get_by_name(self, name:str) -> BasePlant:
        return self.db_session.query(self.model).filter_by(name=name).one()
    
    def add(self, instance: BasePlant) -> None:
        self.db_session.add(instance)
"""
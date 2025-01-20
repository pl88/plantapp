from sqlalchemy.orm import Session

from database.session import get_db
from models.plant import Plant


class PlantRepository:
    db_session: Session
    model: Plant = Plant

    def __init__(self, db_session: Session = None) -> None:
        self.db_session = db_session or next(get_db())

    def get_by_name(self, name: str) -> Plant:
        return self.db_session.query(self.model).filter_by(name=name).one()

    def add(self, instance: Plant) -> None:
        self.db_session.add(instance)

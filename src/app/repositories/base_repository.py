from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from database.session import get_db
from models.base_plant import BasePlant


class BasePlantRepository:
    db_session: Session
    model: BasePlant = BasePlant

    def __init__(self, db_session: Session = None) -> None:
        self.db_session = db_session or next(get_db())

    def get_by_name(self, name: str) -> BasePlant:
        try:
            resp = self.db_session.query(self.model).filter_by(name=name).one()
        except NoResultFound:
            raise
        except Exception:
            raise

        return resp

    def add(self, instance: BasePlant) -> None:
        self.db_session.add(instance)

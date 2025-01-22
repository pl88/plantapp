from sqlalchemy.orm import declarative_base


class Base:
    pass


BaseModel = declarative_base(cls=Base)

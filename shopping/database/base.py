from sqlalchemy.orm import DeclarativeBase

#enable sqlAlchemy to create and map objects to records
class Base(DeclarativeBase):
    pass

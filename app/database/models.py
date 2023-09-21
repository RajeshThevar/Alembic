from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship, sessionmaker, Session, declarative_base, as_declarative
from pydantic import BaseModel
import datetime, psycopg2, typing

Base = declarative_base()



class_registry: typing.Dict = {}

@as_declarative(class_registry= class_registry)
class Base:
    id: typing.Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

#SQLAlchemy model
class Business(Base):
    __tablename__ = "business"

    business_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    business_name = Column(String(256), nullable=False)
    symptom_code = Column(String(256), nullable=False)
    symptom_name = Column(String(256), nullable=False)
    symptom_diagnostic = Column(String(256), nullable=False)


class RequestModel(BaseModel):
    business_id: int
    business_name: str
    symptom_code: str
    symptom_name: str
    symptom_diagnostic: str

class ResponseModel(RequestModel):
    ...

# business_data = RequestModel()
from sqlalchemy import DECIMAL, TEXT, VARCHAR, Column, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Dealer(Base):
    __tablename__ = "dealer"

    id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True,
    )
    dealer_name = Column(VARCHAR(255), nullable=False, unique=True)
    address = Column(TEXT)
    phone = Column(VARCHAR(10))


class Car(Base):
    __tablename__ = "car"

    id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True,
    )
    model = Column(VARCHAR(255), nullable=False)
    year = Column(Integer)
    color = Column(VARCHAR(10))
    mileage = Column(Integer)
    price = Column(DECIMAL(8, 2))
    dealer_id = Column(Integer, ForeignKey("dealer.id"))

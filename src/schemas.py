from typing import Optional

from pydantic import BaseModel


class NewDealer(BaseModel):
    dealer_name: str
    address: Optional[str]
    phone: Optional[str]


class ChangeDealer(BaseModel):
    dealer_name: Optional[str]
    address: Optional[str]
    phone: Optional[str]


class SearchDealer(BaseModel):
    id: Optional[int]
    dealer_name: Optional[str]
    address: Optional[str]
    phone: Optional[str]


class NewCar(BaseModel):
    model: str
    year: Optional[int]
    color: Optional[str]
    mileage: Optional[int]
    price: Optional[float]
    dealer_id: int


class ChangeCar(BaseModel):
    model: Optional[str]
    year: Optional[int]
    color: Optional[str]
    mileage: Optional[int]
    price: Optional[float]
    dealer_id: Optional[int]


class SearchCar(BaseModel):
    id: Optional[int]
    model: Optional[str]
    year: Optional[int]
    color: Optional[str]
    mileage: Optional[int]
    price: Optional[float]
    dealer_id: Optional[int]

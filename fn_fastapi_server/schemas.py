from typing import Dict, List, Set, Optional
from pydantic import BaseModel
from pydantic.errors import cls_kwargs
from pydantic.types import Json
from sqlalchemy.sql.sqltypes import Boolean

class All_work_ordersCreate(BaseModel):
    order_id: int
    start_date: str
    start_time:str
    type: str
    hours: int
    rate: int
    location: str
    title: str

class All_work_orders(BaseModel):
    # id: int
    order_id: int
    start_date: str
    start_time:str
    type: str
    hours: int
    rate: int
    location: str
    title: str
    class Config:
        orm_mode = True

class Users_infoCreate(BaseModel):
    chat_id: int
    username: str
    filter_pattern: Optional[int] = 1
    send_to_bot: Optional[int] = 0
    desired_date_from: Optional[str] = "2021-01-01"
    desired_date_until: Optional[str] = "9999-99-99"
    desired_time: Optional[str] = "01:01:01"
    desired_rate: Optional[int] = 1

class Users_infoUpdate(BaseModel):
    filter_pattern: Optional[int]
    send_to_bot: Optional[int]
    desired_date_from: Optional[str]
    desired_date_until: Optional[str]
    desired_time: Optional[str]
    desired_rate: Optional[int]

class Users_info(BaseModel):
    chat_id: int
    username: str
    filter_pattern: int
    send_to_bot: int
    desired_date_from: str
    desired_date_until: str
    desired_time: str
    desired_rate: int
    class Config:
        orm_mode = True

class Secrets_create(BaseModel):
    name: str
    username: str
    password: str
    access_token: str
    refresh_token: str

class Secrets_update(BaseModel):
    name: Optional[str]
    username: Optional[str]
    password: Optional[str]
    access_token: Optional[str]
    refresh_token: Optional[str]

class Secrets(BaseModel):
    name: str
    username: str
    password: str
    access_token: str
    refresh_token: str


class Bar(BaseModel):
    order_id: int
    start_date: str
    start_time: str
    type: str
    hours: int
    rate: int
    location: str
    title: str
    def __init__(self, **kwargs):
        kwargs["order_id"] = kwargs["pay"]["work_order_id"]
        kwargs["start_date"] = kwargs["schedule"]["service_window"]["start"]["local"]["date"]
        kwargs["start_time"] = kwargs["schedule"]["service_window"]["start"]["local"]["time"]
        kwargs["type"] = kwargs["pay"]["type"]
        kwargs["hours"] = kwargs["pay"]["base"]["units"]
        kwargs["rate"] = kwargs["pay"]["base"]["amount"]
        kwargs["location"] = kwargs["location"]["city"] +", "+ kwargs["location"]["state"]
        super().__init__(**kwargs)    

class Work_orders(BaseModel):
    results: List[Bar]
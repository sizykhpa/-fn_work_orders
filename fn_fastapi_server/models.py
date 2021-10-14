from typing import Dict
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from database import Base

class All_work_orders(Base):
    __tablename__ = "all_work_orders"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, unique=True, index=True)
    start_date = Column(String, unique=False, index=True)
    start_time = Column(String, unique=False, index=True)
    type = Column(String, unique=False, index=True)
    hours = Column(Integer, unique=False, index=True)
    rate = Column(Integer, unique=False, index=True)
    location = Column(String, unique=False, index=True)
    title = Column(String, unique=False, index=True)

class Users_info(Base):
    __tablename__ = "users_info"
    
    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    filter_pattern = Column(Integer, unique=False, index=True)
    send_to_bot = Column(Integer, unique=False, index=True)
    desired_date_from = Column(String, unique=False, index=True)
    desired_date_until = Column(String, unique=False, index=True)
    desired_time = Column(String, unique=False, index=True)
    desired_rate = Column(Integer, unique=False, index=True)


class Secrets(Base):
    __tablename__ = "secrets"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String, unique=True, index=True)
    access_token = Column(String, unique=True, index=True)
    refresh_token = Column(String, unique=True, index=True)


    




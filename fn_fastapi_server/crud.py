from sqlalchemy.orm import Session, session
from sqlalchemy import and_
import sqlalchemy
import json
from sqlalchemy.sql.expression import update
import models, schemas


#####################################################################################
#                              WORK ORDERS                                          #
#####################################################################################

def get_work_order_by_orderid(db: Session, order_id: int):
    return db.query(models.All_work_orders).filter(models.All_work_orders.order_id == order_id).first()

def get_all_work_orders(db: Session, skip: int, limit: int):
    asc_expression = sqlalchemy.sql.expression.asc(models.All_work_orders.start_date)
    return db.query(models.All_work_orders).order_by(asc_expression).offset(skip).limit(limit).all()

def get_length(db: Session):
    return len(db.query(models.All_work_orders).all())

def add_work_order(db: Session, work_order: schemas.All_work_ordersCreate):
    db_work_orders = models.All_work_orders(order_id=work_order.order_id,
                                            start_date=work_order.start_date,
                                            start_time=work_order.start_time,
                                            type=work_order.type,
                                            hours=work_order.hours,
                                            rate=work_order.rate,
                                            location=work_order.location,
                                            title=work_order.title
                                            )
    db.add(db_work_orders)
    db.commit()
    db.refresh(db_work_orders)
    return db_work_orders

def add_work_orders_from_fn_api_response(db: Session, all_work_orders):
    db.query(models.All_work_orders).delete()
    db.commit()
    for order in all_work_orders:
        work_order = db.query(models.All_work_orders).filter(models.All_work_orders.order_id == order.order_id).first()
        if work_order is None:
            db_work_order = models.All_work_orders(order_id=order.order_id,
                                                   start_date=order.start_date,
                                                   start_time=order.start_time,
                                                   type=order.type,
                                                   hours=order.hours,
                                                   rate=order.rate,
                                                   location=order.location,
                                                   title=order.title
                                                   )
            db.add(db_work_order)
            db.commit()
    return all_work_orders

def clear_table_all_work_orders(db: Session):
    db.query(models.All_work_orders).delete()
    db.commit()



#####################################################################################
#                              Users Info                                           #
#####################################################################################

#start#Users info db
#Get one user by chat id
def get_user_from_users_info_by_chatid(db: Session, chat_id: int):
    return db.query(models.Users_info).filter(models.Users_info.chat_id == chat_id).first()

#Get all users
def get_all_users_info(db: Session):
    return db.query(models.Users_info).all()

#Create new user
def create_user_info(db: Session, user: schemas.Users_infoCreate):
    db_user = models.Users_info(chat_id=user.chat_id,
                                username=user.username,
                                filter_pattern=user.filter_pattern,
                                send_to_bot=user.send_to_bot,
                                desired_date_from=user.desired_date_from,
                                desired_date_until=user.desired_date_until,
                                desired_time=user.desired_time,
                                desired_rate=user.desired_rate
                                )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#update a user info
def update_user_value(db: Session, chat_id: int, values: schemas.Users_infoUpdate):
    new_values_dict = values.dict()
    for key in new_values_dict:
        if new_values_dict[key] is not None:
            db.query(models.Users_info).filter(models.Users_info.chat_id == chat_id).update({key: new_values_dict[key]})
            db.commit()
    return db.query(models.Users_info).filter(models.Users_info.chat_id == chat_id).first()

#Delete one user
def remove_user_from_users_info_by_chatid(db: Session, chat_id: int):
    db_user = db.query(models.Users_info).filter(models.Users_info.chat_id == chat_id).first()
    if db_user is not None:
        db.delete(db_user)
        db.commit()    

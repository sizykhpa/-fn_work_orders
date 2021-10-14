import asyncio
from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas, requests_to_fn
from database import SessionLocal, engine
     
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#####################################################################################
#                              WORK ORDERS                                          #
#####################################################################################

#Start# Work with work orders
#get work order by id
@app.get("/work_orders/{order_id}", response_model=schemas.All_work_orders)
def et_work_order_by_orderid(order_id: int, db: Session = Depends(get_db)):
    work_order_by_id = crud.get_work_order_by_orderid(db, order_id=order_id)
    return work_order_by_id

#get all work orders
@app.get("/work_orders/", response_model=List[schemas.All_work_orders])
def get_all_work_orders(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    all_work_orders = crud.get_all_work_orders(db, skip=skip, limit=limit)
    return all_work_orders

#get number of work orders 
@app.get("/work_orders/length/")
def add_work_order(db: Session = Depends(get_db)):
    return crud.get_length(db)

#add a work order
@app.post("/work_orders/", response_model=schemas.All_work_orders)
def add_work_order(work_order: schemas.All_work_ordersCreate, db: Session = Depends(get_db)):
    return crud.add_work_order(db=db, work_order=work_order)

#clear the wok orders DB
@app.delete("/clear_work_orders/")
def clear_all_work_orders(db: Session = Depends(get_db)):
    return crud.clear_table_all_work_orders(db=db)
 
#Send reqest to the FN API server and save results to the DB
@app.get("/send_request_to_fn/", response_model=List[schemas.All_work_orders])
def test(db: Session = Depends(get_db)):
    try:
        raw_data = requests_to_fn.get_all_work_orders()
        all_work_orders = schemas.Work_orders.parse_obj(raw_data).results
        return crud.add_work_orders_from_fn_api_response(db=db, all_work_orders=all_work_orders)  
    except ValueError:
        raise HTTPException(status_code=500, detail='Failed to get the correct response')
    except:
        raise HTTPException(status_code=500, detail='Error, the work orders cannot be obtained')
 
#end   

#####################################################################################
#                              Users Info                                           #
#####################################################################################

#start#Work with users info
#get all users
@app.get("/users_info/", response_model=List[schemas.Users_info])
def get_all_users_info(db: Session = Depends(get_db)):
    all_users_info = crud.get_all_users_info(db)
    return all_users_info

#get one user by chat id
@app.get("/users_info/{chat_id}", response_model=schemas.Users_info)
def get_user_from_users_info(chat_id: int, db: Session = Depends(get_db)):
    user_by_chat_id = crud.get_user_from_users_info_by_chatid(db, chat_id=chat_id)
    return user_by_chat_id

#create new user
@app.post("/users_info/", response_model=schemas.Users_info)
def create_user_info(user: schemas.Users_infoCreate, db: Session = Depends(get_db)):
    return crud.create_user_info(db=db, user=user)   

#Update user value  
@app.put("/users_info/{chat_id}", response_model=schemas.Users_info)
def update_user_value(chat_id: int, values: schemas.Users_infoUpdate, db: Session = Depends(get_db)):
    return crud.update_user_value(db=db, chat_id=chat_id, values=values) 

#delete user by chat id
@app.delete("/users_info/{chat_id}")
def remove_printer_from_list(chat_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_from_users_info_by_chatid(db, chat_id=chat_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        data1 = { "chat id": f"{db_user.chat_id}", "status": "removed"}
    crud.remove_user_from_users_info_by_chatid(db, chat_id=chat_id)
    return data1
#end#    
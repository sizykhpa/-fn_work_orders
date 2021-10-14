from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import filters

import markup as nav
from vardata import FN_bot_data, parse_commands_string
import vardata

import requests
import json
import asyncio
import time

bot = Bot(FN_bot_data.BOT_TOKEN)
dp = Dispatcher(bot)


async def new_f():
    if FN_bot_data.status == 1:
        print(time.strftime('%X'))
        
        try:
            work_orders = await vardata.req_async()
            print(work_orders[1])
            users_list = await vardata.get_users_list()
            for user in users_list:
                if user["send_to_bot"] == 1:
                    await bot.send_message(int(user["chat_id"]), json.dumps(work_orders[1]))

        except:
            await bot.send_message(FN_bot_data.admin_chat_id, work_orders)
            FN_bot_data.status = 0
            await bot.send_message(FN_bot_data.admin_chat_id, "app stopped")
            raise
            
        await asyncio.sleep(20)

async def main():
    while True:
        await new_f()
        await asyncio.sleep(delay=0)

#Handles the /start command
@dp.message_handler(commands=['start'])
async def on_message(message: types.Message):
    await message.reply('Menu button added', reply_markup = nav.main_menu)      
    if message.text == "/start":
        await bot.send_message(message.chat.id, "Send command /get_my_info")

#Administrator commands
@dp.message_handler(filters.Text(startswith=FN_bot_data().admin_commands_list(), ignore_case=True), filters.builtin.IDFilter(user_id=[FN_bot_data.admin_chat_id]))
async def on_message(message: types.Message):
    mess = message.text
    commands = FN_bot_data()
    #start#Start and stop sending requests to Field Nation
    if mess == commands.start_app or mess == commands.start_app_btn:
        FN_bot_data.status = 1
        await bot.send_message(message.chat.id, f"app_started, status is {FN_bot_data.status}") 
    elif mess == commands.stop_app or mess == commands.stop_app_btn:
        FN_bot_data.status = 0
        await bot.send_message(message.chat.id, f"app_stopped, status is {FN_bot_data.status}") 
    #end#  
    #opens admin menu
    elif mess == 'Admin' or mess == 'admin':
        await message.reply('Admin menu', reply_markup = nav.admin_menu)

#Users commands
@dp.message_handler(filters.Text(startswith=FN_bot_data().commands_list(), ignore_case=True))
async def on_message(message: types.Message):
    mess = message.text
    commands = FN_bot_data()
    
    #The main menu command
    if mess == 'Main menu':
        await message.reply('You are at the main menu', reply_markup = nav.main_menu)

    #start#Enable/Disable notifications
    elif mess == commands.start_notify or mess == commands.start_notify_btn:
        FN_bot_data.users_dict[message.chat.id] = 1
        await bot.send_message(message.chat.id, "notifications_started") 
    elif mess == commands.stop_notify or mess == commands.stop_notify_btn:
        FN_bot_data.users_dict[message.chat.id] = 0
        await bot.send_message(message.chat.id, "notifications_stopped")
    #end#

    #Help command
    elif mess == commands.help or mess == commands.help_btn:
        await bot.send_message(message.chat.id, FN_bot_data.help_info) 

    elif mess == "/get_my_info":
        info = 'Chat ID is: ' + str(message.chat.id) + ', username is: ' + message.chat.username
        await bot.send_message(message.chat.id, info)       

#The filtered orders command
@dp.message_handler(filters.Text(startswith=[FN_bot_data().filtered_orders, FN_bot_data().filtered_orders_btn], ignore_case=True))
async def on_message(message: types.Message):
    print(message.chat.id)
    length = int(requests.get("http://fn_fastapi_server:8005/work_orders/length/").text)
    number_of_orders_count = 0
    for skip in range(0, length, FN_bot_data.number_of_orders):
        work_orders = requests.get(f"http://fn_fastapi_server:8005/work_orders/?skip={skip}&limit={FN_bot_data.number_of_orders}")
        resp = json.loads(work_orders.text)
        mess = ""
        for order in resp:
            if order["start_date"] < "2021-10-10":       
                new = ' | '.join(map(str, list(order.values())))
                mess = mess + new + "\n" + "-   -   -   -   -" + "\n"
                number_of_orders_count += 1
        if mess != "":
            await bot.send_message(message.chat.id, mess)
    #sends a message with total number of orders        
    await bot.send_message(message.chat.id, "Total filtered orders: " + str(number_of_orders_count))        


@dp.message_handler(filters.Text(startswith=['add_user', 'set'], ignore_case=True))
async def on_message(message: types.Message):
    print(message.chat.id)
    mess = message.text.lower()
    if "set" in mess:
        payload = parse_commands_string(mess, 'set')
        if payload is not False:
            url = f'http://fn_fastapi_server:8005/users_info/{message.chat.id}'
            r = requests.put(url, data = json.dumps(payload))
            await bot.send_message(message.chat.id, r.text)
        else:
            await bot.send_message(message.chat.id, "Wrong command")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.create_task(executor.start_polling(dp, skip_updates=True))
    loop.run_forever()

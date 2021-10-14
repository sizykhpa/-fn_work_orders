from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from vardata import FN_bot_data

btn_main = KeyboardButton('Main menu')

btn_help = KeyboardButton(FN_bot_data().help_btn)
btn_start_notify = KeyboardButton(FN_bot_data().start_notify_btn)
btn_stop_notify = KeyboardButton(FN_bot_data().stop_notify_btn)
btn_filtered_orders = KeyboardButton(FN_bot_data().filtered_orders_btn)
btn_settings = KeyboardButton(FN_bot_data().settings_btn)
main_menu = ReplyKeyboardMarkup(resize_keyboard = True).add(btn_help, btn_start_notify, btn_stop_notify, btn_filtered_orders, btn_settings)


btn_info = KeyboardButton('Info')
btn_money = KeyboardButton('Money')
other_menu = ReplyKeyboardMarkup(resize_keyboard = True).add(btn_info, btn_money, btn_main)


#Administrator menu
btn_start_app = KeyboardButton(FN_bot_data().start_app_btn)
btn_stop_app = KeyboardButton(FN_bot_data().stop_app_btn)
btn_add_user = KeyboardButton(FN_bot_data().add_user_btn)
btn_admin = KeyboardButton('Admin')
admin_menu = ReplyKeyboardMarkup(resize_keyboard = True).add(btn_start_app, btn_stop_app, btn_add_user, btn_main)
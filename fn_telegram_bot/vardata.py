import os
import aiohttp

with open('.env', 'r') as file:
    for line in file.readlines():
        values = line.replace('\n', '').split("=")
        os.environ[values[0]] = values[1]

class FN_bot_data:
    status = 0
    help_info = "show filtered orders: /f_orders \nshow all orders: /all_orders\nshow your info: /get_my_info\nstart notifications: /start_notify\nstop notifications: /stop_notify"
    number_of_orders = 15
    BOT_TOKEN = os.environ['BOT_TOKEN']
    admin_chat_id = os.environ['ADMIN_CHAT_ID']

    def __init__(self):

        #all users commands
        self.help = '/help'
        self.help_btn = 'Help'
        
        self.start_notify = '/start_notify'
        self.start_notify_btn = 'Start notify'
        
        self.stop_notify = '/stop_notify'
        self.stop_notify_btn = 'Stop notify'
        
        self.filtered_orders = '/f_orders'
        self.filtered_orders_btn = 'Filtered Orders'
        
        self.settings_btn = 'Settings'
        
        #admin commands
        self.start_app = '/start_app'
        self.start_app_btn = 'Start app'
        self.stop_app = '/stop_app'
        self.stop_app_btn = 'Stop app'
        self.add_user = '/add_users'
        self.add_user_btn = 'Add user'
        #end

    def commands_list(self):
        return [self.start_notify, self.start_notify_btn, self.stop_notify, self.stop_notify_btn, self.help, self.help_btn, '/get_my_info', 'Main menu', self.settings_btn]

    def admin_commands_list(self):
        return [self.start_app, self.start_app_btn, self.stop_app, self.stop_app_btn, self.add_user, self.add_user_btn, 'Admin', 'admin']


def parse_commands_string(str, command):
    dict = {}
    try:
        str_list = str.replace(command, "").replace(" ", "").split(',')
        for command in str_list:
            command = command.split('=')
            dict[command[0]] = command[1]
        return dict    
    except:
        return False   


async def req_async():
    async with aiohttp.ClientSession() as session:
        url = "http://fn_fastapi_server:8005/send_request_to_fn/"
        async with session.get(url) as resp:
            result = await resp.json()
            return result


async def get_users_list():
    async with aiohttp.ClientSession() as session:
        url = "http://fn_fastapi_server:8005/users_info/"
        async with session.get(url) as resp:
            result = await resp.json()
            return result


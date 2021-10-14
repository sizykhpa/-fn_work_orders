import requests
import json
import os
from vardata import Request_data

token_expired = 'You must provide a valid OAuth token to make a request'

refresh_token = os.environ['REFRESH_TOKEN']
username = os.environ['FN_USERNAME']
password = os.environ['FN_PASSWORD']                


def get_all_work_orders():
    try:
        url, headers = Request_data().all_work_orders(os.environ['ACCESS_TOKEN'])
        response = requests.get(url, headers=headers)

        if response.text == token_expired:
            print("Token expired")
            refresh_fn()
            url, headers = Request_data().all_work_orders(os.environ['ACCESS_TOKEN'])
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                return json.loads(response.text)
            else:
                raise ValueError('Err1. Failed to get the correct response')
        
        elif response.status_code == 200:          
            return json.loads(response.text)
        else:
            raise ValueError('Err2. Failed to get the correct response')
    
    except:
        raise ValueError('Err3. Failed to get the correct response')        

def login_fn():
    url, headers, body = Request_data().login_fn(username, password)
    response = requests.post(url, headers=headers, data=body)
    print(response.text)

def logout_fn():
    url, headers = Request_data.logout_fn(os.environ['ACCESS_TOKEN'])
    response = requests.delete(url, headers=headers)
    print(response.text)

def refresh_fn():
    url, headers, body = Request_data().refresh_fn(refresh_token)
    response = requests.post(url, headers=headers, data=body)
    print("Refreshing token")
    print(response.text)
    os.environ['ACCESS_TOKEN'] = json.loads(response.text)["access_token"]


if __name__ == '__main__':
    get_all_work_orders()
    # refresh_fn()

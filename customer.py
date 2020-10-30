import requests
from base_config import *

##Customer class to handle all work done with both source and destination customers
class Customer:
    def __init__(self, token):
        self.url = url_base + "/"
        self.payload = {}
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x-api-key': token
            }

##Get apps from the original customer to be used to create apps on destination customer and copy configs over to
##the corresponding new application
    def get_apps(self):
        self.url = url_base + "/apps"
        self.payload = {}
        try:
            response = requests.get(self.url, headers=self.headers, data = self.payload)
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception
        data = response.json().get('data')
        app_info = []
        for item in data:
            app_info.append((item.get('id'), item.get('name'), item.get('description')))
        return app_info

##Create applications on the destination customer pulled from the source customer
    def create_apps(self, app_name, app_description):
        self.url = url_base + "/apps"
        self.payload = {
            "name": app_name,
            "description": app_description
        }
        try:
            response = requests.get(self.url, headers=self.headers, data = self.payload)
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception
        status = response.json()
        if status == "200 OK":
            print("successfully create: "+ app_name)
        return status
"""
##Get configs from the Original customer
def get_configs():
    pass

##Get appid for apps created on the destination customer
def get_new_app_id():
    url_endpoint = "/apps"
    url = url_base + url_endpoint
    payload = {}
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x-api-key': token_destination
    }
    if token_destination != token_source:
        try:
            response = requests.get(url, headers=headers, data = payload)
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception
        response = response.json()
        name_list = []
        for data in response['data']:
            name_list.append(data['id'])
            return name_list
    else:
        return("destination customer api key: "+ token_destination+ " matches source customer api key: "+ token_source+ ". These should be different. Please validate that you are using the correct API keys for both source and destination.")

##Create configs on the destination customer based on the configs pulled from the original customer
def create_configs():
    pass
"""
import requests
from base_config import *


class Customer:
    def __init__(self, token):
        self.url = url_base + "/"
        self.payload = {}
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x-api-key': token
            }
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

    def creat_apps(self):
        self.url = url_base + "/apps"
        self.payload = {
            "name": app_name,
            "description": app_description
        }

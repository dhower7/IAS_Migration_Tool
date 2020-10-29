import requests
from base_config import *


class Customer:
    def _init_(self, API):
        self.url_endpoint = "/apps"
        self.url = url_base + self.url_endpoint
        self.payload = {}
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x-api-key': token_source
            }
    def get(self):
        response = requests.get(self.url, headers=self.headers, data = self.payload)
        response = response.json()
        print(response)
        return response
 
import requests
from base_config import *


##User Input for required information
token_source = input("Enter Source Customer API Key: ")
token_destination = input("Enter Destination Customer API Key: ")


class SourceEnumeration_Apps:
    def _init_(self, API):
        self.url_endpoint = "/scan-configs"
        self.url = url_base + url_endpoint
        self.payload = {}
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x-api-key': token_source
            }
    def get(self):
        response = requests.get(self.url, headers=self.headers, data = self.payload)
        print(response.text.encode('utf8'))
 
source = SourceEnumeration_Apps()
print(source.get())
       

""" import source applications
import source configs
download source files

##destination provisioning
create application
use source application name and description
create configurations in application_destination using configid_source 
use source configuration name and description
response = requests.get("") 
"""
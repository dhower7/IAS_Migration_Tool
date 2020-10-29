import requests
import json
from customer import Customer

token_source = ""
token_destination = ""
app_name_source = ""
appid_destination = ""
configid_source = ""
configid_destination = ""
url_base = "https://us.api.insight.rapid7.com/ias/v1"

"""
##User Input for required information
token_source = input("Enter Source Customer API Key: ")
token_destination = input("Enter Destination Customer API Key: ")
"""
source_customer = Customer(token_source)
destination_customer = Customer(token_destination)

source_customer.get()
destination_customer.get()


"""
def get_applications():
    url_endpoint = "/apps"
    url = url_base + url_endpoint
    payload = {}
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x-api-key': token_source
    }
    if token_source != token_destination:
        try:
            response = requests.get(url, headers=headers, data = payload)
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception

        response = response.json()
        data = response
        return data

    else:
        return("destination customer api key: "+ token_destination+ " matches source customer api key: "+ token_source+ ". These should be different. Please validate that you are using the correct API keys for both source and destination.")
"""

"""
        name_list = []
        for data in response['data']:
            name_list.append(data)
        return name_list
"""
"""
a = get_applications()

for key, value in a(data):
    print(key, ' : ', value)

    
def get_configs():
    pass
def create_applications():
    while app_name_source != "":
        url_endpoint = "/apps"
        url = url_base + url_endpoint
        payload = {'name': app_name_source, 'description': ""}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x-api-key': token_destination
            }
        try:
            response = requests.request("POST", url, headers=headers, data = payload)
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception
        
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

def creat_configs():
    pass

#app_name_source = get_applications()

"""
"""
while app_name_source > 0:
    for app in app_name_source
print(app_name_source['id'])
app_creation_response = create_applications()
print(app_creation_response)
"""

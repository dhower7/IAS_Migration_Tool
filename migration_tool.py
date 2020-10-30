import requests
import json
from customer import Customer


##User Input for required information
token_original = input("Enter Original Customer API Key: ")
token_destination = input("Enter Destination Customer API Key: ")

#enumerate_origin_apps = Customer(token_original)
enumerate_origin_apps = Customer('0c47f4a0-a3a5-411c-9e6b-149190618560')
if token_source != "":
    enumerate_origin_apps.get_apps()
else:
    print("Original Customer API Key is missing.")

create_destination_apps = Customer(token_destination)
#create_destination_apps = Customer('insert static api key')
if token_destination != "":
    create_destination_apps.create_apps()
else:
    print("Destination Customer API Key is missing.")

"""
destination_customer = Customer(token_destination)
destination_customer.create_apps()
"""

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

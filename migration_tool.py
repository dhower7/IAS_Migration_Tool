import requests
import json
from customer import Customer


##User Input for required information
#token_original = input("Enter Original Customer API Key: ")
#token_destination = input("Enter Destination Customer API Key: ")

## Use predefined API Keys
## use Razordemo -> "Applied Engineering - US" API Key for original customer 
token_original = ('0f6352ba-107b-48ea-9f7d-a3d536eb4dd3')
## Use Razordemo -> "Specialists Research" API Key for Destination
token_destination = ('0c47f4a0-a3a5-411c-9e6b-149190618560')


##Enumerate applications in the original customer
enumerate_origin_apps = Customer(token_original)
if token_original != "":
    enumerate_origin_apps.get_apps()
    app_list = enumerate_origin_apps.get_apps()
else:
    print("Original Customer API Key is missing.")

#print(app_list[0])

#for id in app_list(id, name, description):
#    print(id)

#apps = list(enumerate(app_list, start=1))
def app_info():
    app_id = []
    app_name = []
    app_description = []
    for ids in app_list:
        for id in app_info:
            app_id.append(id)
        app_name.append(names)
        app_description.append(descriptions)
    print(app_id)
    print(app_name)
    print(app_description)
    
print(type(app_list))


#app_description.append((descriptions.get([2]))

"""

##Create applications pulled from the original customer into the destination customer
create_destination_apps = Customer(token_destination, app_list)
if token_destination != "":
    create_destination_apps.create_apps()
else:
    print("Destination Customer API Key is missing.")
"""

## Todo psuedo code ##

"""    
def get_configs():
    pass

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

def create_configs():
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

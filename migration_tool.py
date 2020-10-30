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

#print(app_list)

##Enumerate app_list to create a list of apps with their appid, name and description
##This will be used to feed back into the customer class to tell the create_apps function what apps to create
##Is this the correct place to put this or should this work be done in the Customer class??

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

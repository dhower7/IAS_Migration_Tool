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
#    enumerate_origin_apps.get_apps()
    app_enumeration = enumerate_origin_apps.get_apps()
else:
    print("Original Customer API Key is missing.")

#print(app_enumeration)

create_app_in_customer_destination = Customer(token_destination)
for app in app_enumeration:
    create_app_in_customer_destination.create_apps(app['name'], app.get('description', " "))

enumerate_origin_configs = Customer(token_original)
if token_original != "":
for id in app_enumeration:
    config_enumeration = enumerate_origin_configs.get_apps()
else:
    print("Original Customer API Key is missing.")

"""

##Enumerate app_list to create a list of apps with their appid, name and description
##This will be used to feed back into the customer class to tell the create_apps function what apps to create
##Is this the correct place to put this or should this work be done in the Customer class??

#app_name = [app_enumeration]

#print(app_info(app_enumeration))

##Pseudocode for remaining requirements

"""
"""

## Not sure if we should do this ##
- pull users from old customer -> user_list
    - user_list - content
        - user name
        - user email

- iterate through apps to pull configs from each app -> config_list
    - config_list - content
        - config name

- iterate through scan_configs from each app and create configs in each app on destination customer -> scan_configs

- iterate through scan_configs from each app on original customer and output files to tmp directory

- iterate through scan_configs from each app and upload files from tmp directory to destination customer -> file id's
    - file_ids - content
        - file name (represented by file id)

- iterate through scan config options from each scan config in each app -> scan_config_options
    - scan_config_options - content
        - config json blob


- pull app ids and names from new customer -> app_list_new
    - app_list_new - content
        - app id
        - app name

- upload files from old customer to new customer

- create configs in new customer based on config name in config_list

"""
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
    app_enumeration = enumerate_origin_apps.get_base()
else:
    print("Original Customer API Key is missing.")

print(app_enumeration)


"""
## Create Apps in Customer Destination

create_app_in_customer_destination = Customer(token_destination)
for app in app_enumeration:
    app_creation = create_app_in_customer_destination.create_base(app['name'], app.get('description', " "))
    ##create_app_in_customer_destination.create_apps(app['name'], app.get('description', " "))
"""
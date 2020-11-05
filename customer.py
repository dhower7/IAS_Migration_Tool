import requests

url_base = "https://us.api.insight.rapid7.com/ias/v1"

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
<<<<<<< Updated upstream
        self.url = url_base + "/apps"
        self.payload = {}
=======
        print("Getting Apps")
        url = f"{url_base}/apps"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception
        data = response.json().get('data')
        ## enumerate configs
        for app_data in data:
            app_data['configs'] = self.get_configs(app_data['id'])
        return data

        ## get sub data
    def get_configs(self, app_id):
        print("Getting Configs")
        url = f"{url_base}/search"
        payload = {
            "query": f"scanconfig.app.id = '{app_id}'",
            "type": "SCAN_CONFIG"
            }
        try:
            response = requests.post(url, headers=self.headers, json = payload)
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception

        data = response.json().get('data')
        ## file enumeration
        for config in data:
            #app_id = self.get_files(app_id)
            config['files'] = self.get_files(app_id)
            config['config_options'] = self.get_config_options(config['id'])
        return data
    
    def get_files(self, app_id):
        print("Getting Files")
        url = f"{url_base}/apps/{app_id}/files"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception
        data = response.json().get('data')
        return data
           
    def download_files(self, file_id):
        print("Downloading Files")
        pass
    
    def get_config_options(self, config_id):
        print("Getting Config Options:")
        #doesn't seem to be passing config ids
        import pdb; pdb.set_trace()
        url = f"{url_base}/scan-configs/{config_id}/options"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception
        data = response.json().get('data')

    def get_engine_groups(self):
        print("Getting Engine Groups")
        url = f"{url_base}/engine-groups"
>>>>>>> Stashed changes
        try:
            response = requests.get(self.url, headers=self.headers, data = self.payload)
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception
        data = response.json().get('data')
        #print("API Token-1: "+ str(self.token))
        return data

    ##Create applications on the destination customer pulled from the source customer
    def create_apps(self, app_name, app_description):
        self.url = url_base + "/apps"
        self.payload = ('{"name": ' + str(app_name) + ', "description": ' + str(app_description) + '}')
        response = requests.post(self.url, headers=self.headers, data = self.payload)
        print(response.text.encode('utf8'))
        #print("API Token: "+ str(self.token))

        location = response.headers.get('Location', None)
        if location:
            print("successfully create: "+ app_name)
        return 

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
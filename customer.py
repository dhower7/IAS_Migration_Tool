import requests

url_base = "https://us.api.insight.rapid7.com/ias/v1"

##Customer class to handle all work done with both source and destination customers
class Customer:
    def __init__(self, token):
        self.url = url_base + '/'
        self.payload = {}
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x-api-key': token
            }

##Get apps from the original customer to be used to create apps on destination customer and copy configs over to
##the corresponding new application
    def get_apps(self):
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
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception
        data = response.json().get('data')
        """
        ## enumerate configs
        for app_data in data:
            app_data['configs'] = self.get_configs(app_data['id'])
        """
        return data

    def get_attack_templates(self):
        print("Getting Attack Templates")
        url = f"{url_base}/attack-templates"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception
        data = response.json().get('data')
        """
        ## enumerate configs
        for app_data in data:
            app_data['configs'] = self.get_configs(app_data['id'])
        """

    def get_schedules(self):
        print("Getting Schedules")
        url = f"{url_base}/schedules"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception
        data = response.json().get('data')
        """
        ## enumerate configs
        for app_data in data:
            app_data['configs'] = self.get_configs(app_data['id'])
        """

    def get_blackouts(self):
        print("Getting Blackouts")
        url = f"{url_base}/blackouts"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception
        data = response.json().get('data')
        """
        ## enumerate configs
        for app_data in data:
            app_data['configs'] = self.get_configs(app_data['id'])
        """
    """
    ##Create applications on the destination customer pulled from the source customer
    def create_apps(self, app_name, app_description):
        print("Creating Apps:")
        url = f"{url_base}/apps"
        payload = {
            "name": f"{app_name}",
            "description": f"{app_description}""
            }
        response = requests.post(url, headers=self.headers, json = payload)
        print(payload)
        print(response.text.encode('utf8'))

        location = response.headers.get('Location', None)
        if location:
            print("successfully create: "+ app_name)
        return 

    ##Create configs on the destination customer based on the configs pulled from the original customer
    def create_configs():
        print("Creating Configs:")
        url = f"{url_base}/scan-configs"
        payload = {
            "app": {
                f"{app_id}"
                },
            "attack_template": {
                f"{attack_template}""
            "name": f"{config_name}",
            }
        response = requests.post(url, headers=self.headers, json = payload)
        print(payload)
        print(response.text.encode('utf8'))
        return 
    
    def create_files():
        print("Creating Files:")
        url = f"{url_base}/apps/{app_id}/files"
        payload = {f"{"}
        response = requests.post(url, headers=self.headers, json = payload)
        print(payload)
        print(response.text.encode('utf8'))

    def upload_files():
        print("Uploading Files:")
        url = f"{url_base}/scan-configs"
        payload = {
            "app": {
                f"{app_id}"
                },
            "attack_template": {
                f"{attack_template}""
            "name": f"{config_name}",
            }
        response = requests.post(url, headers=self.headers, json = payload)
        print(payload)
        print(response.text.encode('utf8'))

    #refactor due to file id's changing when creating in new system
    #add Content-Type: applciation/octet-stream 
    def update_config_options():
        print("Updating Configs Options:")
        url = f"{url_base}/scan-configs/{config_id}/options"
        payload = {f"{config_options}"}
        response = requests.post(url, headers=self.headers, json = payload)
        print(payload)
        print(response.text.encode('utf8'))
        return 

    def create_engine_groups(self,):
        pass

    def create_attack_templates(self,):
        pass

    def create_schedules(self,):
        pass

    def create_blackouts(self,):
        pass
    """
import requests

url_base = "https://us.api.insight.rapid7.com/ias/v1"

##Customer class to handle all work done with both source and destination customers
class Customer:
    def __init__(self, token):
        self.url = url_base + '/'
        self.payload = {}
        self.token = f"{token}"
        self.data = {}

    def headers(self):
        result = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x-api-key': self.token
            }
        return result

    def set_token(self, token):
        self.token = f"{token}"
        return True
    
    def get_base(self):
        self.data['engine_groups'] = self.get_engine_groups()
        self.data['attack_templates'] = self.get_attack_templates()
        self.data['schedules'] = self.get_schedules()
        self.data['blackouts'] = self.get_blackouts()
        self.data['apps'] = self.get_apps()
        return self.data

##Get apps from the original customer to be used to create apps on destination customer and copy configs over to
##the corresponding new application
    def get_apps(self):
        url = f"{url_base}/apps"
        try:
            response = requests.get(url, headers=self.headers())
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
        url = f"{url_base}/search"
        payload = {
            "query": f"scanconfig.app.id = '{app_id}'",
            "type": "SCAN_CONFIG"
            }
        try:
            response = requests.post(url, headers=self.headers(), json = payload)
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception

        data = response.json().get('data')
        ## file enumeration
        for config in data:
            #app_id = self.get_files(app_id)
            config['files'] = self.get_files(app_id)
            config['config options'] = self.get_config_options(config['id'])
        return data
    
    def get_files(self, app_id):
        url = f"{url_base}/apps/{app_id}/files"
        try:
            response = requests.get(url, headers=self.headers())
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception
        data = response.json().get('data')
        return data
           
    def download_files(self, file_id):
        pass
    
    def get_config_options(self, config_id):
        url = f"{url_base}/scan-configs/{config_id}/options"
        try:
            response = requests.get(url, headers=self.headers())
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception
        data = response.json()
        return data


    def get_engine_groups(self):
        url = f"{url_base}/engine-groups"
        try:
            response = requests.get(url, headers=self.headers())
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception
        data = response.json().get('data')
        return data

    def get_attack_templates(self):
        url = f"{url_base}/attack-templates"
        try:
            response = requests.get(url, headers=self.headers())
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception
        data = response.json().get('data')
        return data

    def get_schedules(self):
        url = f"{url_base}/schedules"
        try:
            response = requests.get(url, headers=self.headers())
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception
        data = response.json().get('data')
        return data


    def get_blackouts(self):
        url = f"{url_base}/blackouts"
        try:
            response = requests.get(url, headers=self.headers())
            response.raise_for_status()
        except requests.HTTPError as exception:
            return exception
        data = response.json().get('data')
        return data

    
    ##Create applications on the destination customer pulled from the source customer
    def create_base(self):
        #print("\n\tCreate Data: \n")
        for engine_group in self.data['engine_groups']:
            self.create_engine_groups(engine_group['name'], engine_group['description'])
            #print(engine_group['name'])
            #print(engine_group['description'])
        #return self.data

    def create_engine_groups(self, group_name, group_description):
        print("\n\t\tCreate Engine Groups Function\n")
        print(group_name)
        print(group_description)
        url = f"{url_base}/engine-groups"
        payload = {
            "name": f"{group_name}",
            "description": f"{group_description}"
        }
        try:
            response = requests.post(url, headers=self.headers(), json = payload)
        except requests.HTTPError as exception:
            return exception
        #data = response.json().get('data')
        location = response.headers.get('Location', None)
        print(location)         

        #return data
    """   
    def create_apps(self):
        url = f"{url_base}/apps"
        for app in self.data[apps]:
            app_id = app.id
        payload = {
            "name": f"{self.data[apps]app_name}",
            "description": f"{app_description}"
            }
        response = requests.post(url, headers=self.headers(), json = payload)
        data = response.json().get('data')
        location = response.headers.get('Location', None)
        if location:
        return data

    ##Create configs on the destination customer based on the configs pulled from the original customer
    def create_configs(self):
        url = f"{url_base}/scan-configs"
        payload = {
            "app": {
                f"{app_id}"
                },
            "attack_template": {
                f"{attack_template}"
            },
            "name": f"{config_name}",
            "description": f"{config_description}"
            }
        response = requests.post(url, headers=self.headers(), json = payload)
        data = response.json().get('data')
        return data
    
    def create_files(self):
        url = f"{url_base}/apps/{app_id}/files"
        payload = {f""}
        response = requests.post(url, headers=self.headers(), json = payload)
        data = response.json().get('data')
        return data

    def upload_files(self):
        url = f"{url_base}/scan-configs"
        payload = {
            "app": {
                f"{app_id}"
                },
            "attack_template": {
                f"{attack_template}"
            },
            "name": f"{config_name}",
            }
        response = requests.post(url, headers=self.headers(), json = payload)
        data = response.json().get('data')
        return data

    #refactor due to file id's changing when creating in new system
    #add Content-Type: applciation/octet-stream 
    def update_config_options(self):
        url = f"{url_base}/scan-configs/{config_id}/options"
        payload = {f"{config_options}"}
        response = requests.post(url, headers=self.headers(), json = payload)
        data = response.json().get('data')
        return data

    def create_attack_templates(self):
        response = requests.post(url, headers=self.headers(), json = payload)
        data = response.json().get('data')
        return data
        pass

    def create_schedules(self):
        response = requests.post(url, headers=self.headers(), json = payload)
        data = response.json().get('data')
        return data
        pass

    def create_blackouts(self):
        response = requests.post(url, headers=self.headers(), json = payload)
        data = response.json().get('data')
        return data
        pass

    """
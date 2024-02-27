import requests
from microservice.adapters.input.IAzure_adapter import IAzureAdapter
from interceptors.Impl.Sanitizer import Sanitizer
from configurations.Config import Config

class AzureAdapter(IAzureAdapter):
    def __init__(self, sanitizer = Sanitizer):
        self.url = Config.API_URL
        self.url_workitems = Config.API_AZURE_WORKITEMS
        self.url_projects = Config.API_AZURE_PROJECTS
        self.api_azure_token = Config.API_AZURE_TOKEN
        self.sanitizer = sanitizer
    
    def get_workitems(self):
        session = requests.Session()
        session.auth = ("", self.api_azure_token)
        url = self.url_workitems
        data = {}
        data_aux = {}
        first_time = True

        while True:
            response = session.get(url) 
            if response.status_code == 200:
                data_aux = response.json()
                if first_time:  
                    data = data_aux
                    first_time = False
                else:
                    data_next = data_aux
                    data['value'] = data['value'] + data_next['value']
                
                if '@odata.nextLink' in data_aux:
                    url = data['@odata.nextLink']
                else:
                    break
            else:
                break
        
        data_sanitizer = self.sanitizer.data_sanitizer_workitems(data)
        return  data_sanitizer
    
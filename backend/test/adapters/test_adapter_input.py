import unittest
import json
from unittest.mock import MagicMock, patch
from microservice.adapters.input.Impl.Azure_adapter import AzureAdapter
import os
import sys

print(os.getcwd())
print(sys.path)

class TestAzureAdapter(unittest.TestCase):
    ''''''
    def setUp(self):
        # Configura cualquier configuración necesaria para las pruebas
        self.config_mock = MagicMock()
        self.config_mock.API_URL = "https://example.com"
        self.config_mock.API_AZURE_WORKITEMS = "/workitems"
        self.config_mock.API_AZURE_PROJECTS = "/projects"
        self.config_mock.API_AZURE_TOKEN = "your_token"

    @patch('requests.Session')
    def test_get_workitems_successful(self, session_mock):

        #Arrage
        with open('..\\resources\\data_input.json', 'r') as file:
            data = json.load(file)

        response_mock = MagicMock()
        response_mock.status_code = 200
        response_mock.json.return_value = data

        session_instance = session_mock.return_value
        session_instance.get.return_value = response_mock

        azure_adapter = AzureAdapter(sanitizer=self.sanitizer_mock)
        azure_adapter.url_workitems = "/workitems"

        #Aact
        result = azure_adapter.get_workitems()

        #Assert
        self.sanitizer_mock.data_sanitizer_workitems.assert_called_once_with(data)
        self.assertEqual(result, self.sanitizer_mock.data_sanitizer_workitems.return_value)

if __name__ == '__main__':
    unittest.main()

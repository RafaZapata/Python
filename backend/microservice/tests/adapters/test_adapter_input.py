import unittest
import requests
import json
from unittest.mock import patch, MagicMock
from microservice.adapters.input.Impl.Azure_adapter import AzureAdapter
from microservice.configurations.Config import Config
from microservice.interceptors.Impl.Sanitizer import Sanitizer
from pathlib import Path
import os


class TestAzureAdapter(unittest.TestCase):

    @patch('requests.Session.get')
    # @patch('interceptors.Impl.Sanitizer')
    def test_get_workitems(self, mock_session_get):

        #Arrange
        api_token = 'ascbdefghijklmno'
        Config.API_URL = 'http://api_url.com'
        Config.API_AZURE_WORKITEMS = 'http://azure_workitems_url.com'
        Config.API_AZURE_PROJECTS = 'http://azure_projects_url.com'
        Config.API_AZURE_TOKEN = api_token

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../resources/data_input.json")

        with open(path, 'r') as file:
            data_input = json.load(file)

        mock_session = MagicMock()
        mock_session_get.return_value.status_code = 200
        mock_session_get.return_value.json.return_value = data_input
        mock_session.return_value = mock_session_get

        #Act
        azure_adapter = AzureAdapter()
        result = azure_adapter.get_workitems()
        data = json.loads(result)     

        #Asserts
        workitems_count = len(data["workitems"])
        workitem_ids = [item["WorkItemId"] for item in data["workitems"]]
        workitem_type = set([item["WorkItemType"] for item in data["workitems"]])

        mock_session_get.assert_called_once_with('http://azure_workitems_url.com')
        self.assertIsNotNone(data)
        self.assertEqual(workitems_count, 3)
        self.assertCountEqual(workitem_ids, ["14761-2024-02-08T13:52:52.277-06:00", "17413-2024-02-08T15:33:12.597-06:00", "17417-2024-02-08T16:15:04.237-06:00"])
        self.assertEqual(len(workitem_type), 1)

if __name__ == '__main__':
    unittest.main()

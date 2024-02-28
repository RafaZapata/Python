import unittest
import json
from unittest.mock import patch, MagicMock
from adapters.output.Impl.Elastic_adapter import ElasticsearchCliente
from configurations.Config import Config

class TestElasticsearchCliente(unittest.TestCase):

    def setUp(self):
        Config.ELK_HOST = 'http://elk_host.com'
        Config.ELK_USER = 'elk_user'
        Config.ELK_PWD = 'elk_pwd'
        Config.ELK_INDEX = 'elk_index'

    @patch('elasticsearch.Elasticsearch')
    @patch('elasticsearch.helpers.bulk')
    def test_data_index_bulk_success(self, mock_bulk, mock_elasticsearch):
        
        # Arrange
        mock_es_instance = MagicMock()
        mock_elasticsearch.return_value = mock_es_instance

        mock_bulk.return_value = (0, [])

        # Act
        elastic_client = ElasticsearchCliente()

        with open('../AzureDevOps-Microbatch/tests/resources/data_processor.json', 'r') as file:
            data_processor= file.read()

        result = elastic_client.data_index_bulk(data_processor)

        # Assert
        # mock_elasticsearch.assert_called_once_with(['http://elk_host.com'], http_auth=('elk_user', 'elk_pwd'), headers={'Content-Type': 'application/json'})
        self.assertEqual(result, "ok")

    @patch('elasticsearch.helpers.bulk')
    def test_data_index_bulk_failure(self, mock_bulk):
        
        # Arrange
        mock_bulk.side_effect = Exception("Error en la operación de Elasticsearch")

        # Act
        elastic_client = ElasticsearchCliente()

        with self.assertRaises(Exception) as context:
            elastic_client.data_index_bulk('[{"field": "value"}]')

        self.assertEqual(str(context.exception), "Error en la operación de Elasticsearch")

if __name__ == '__main__':
    unittest.main()

import unittest
import json
from unittest.mock import Mock, patch
from microservice.adapters.output.Impl.Elastic_adapter import ElasticsearchCliente

class TestElasticsearchCliente(unittest.TestCase):

    @patch('microservice.adapters.output.Impl.Elastic_adapter.Elasticsearch')
    @patch('configurations.Config')
    def test_data_index(self, mock_config, mock_elasticsearch):
        
        #Arrange
        mock_config.ELK_HOST = 'https://elasticsearch.example.com'
        mock_config.ELK_USER = 'elasticsearch_user'
        mock_config.ELK_PWD = 'elasticsearch_password'
        mock_config.ELK_INDEX = 'elasticsearch_index'

        mock_elasticsearch_instance = Mock()
        mock_elasticsearch.return_value = mock_elasticsearch_instance

        elastic_client = ElasticsearchCliente()
        
        with open('..\\bronze-microbatch\\tests\\resources\\data_processor.json', 'r') as file:
            input_azure = json.load(file)

        data = json.dumps(input_azure)
        
        #Act
        result = elastic_client.data_index(data)

        #Assert
        self.assertEqual(mock_elasticsearch_instance.index.call_count, 3)

if __name__ == '__main__':
    unittest.main()

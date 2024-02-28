from elasticsearch import Elasticsearch
from microservice.configurations.Config import Config
from elasticsearch.exceptions import ElasticsearchException
from microservice.adapters.output.IElastic_adapter import IElasticAdapter
from elasticsearch import helpers
import json

class ElasticsearchCliente(IElasticAdapter):
    def __init__(self):
        self.es = Elasticsearch(
            [Config.ELK_HOST],
            http_auth=(Config.ELK_USER, Config.ELK_PWD),
            headers={'Content-Type': 'application/json'}
        )
        self.index=Config.ELK_INDEX

    def data_index_bulk(self, documents):
        data = json.loads(documents)
        try:
            workitems = [
                {
                    "_index": self.index,
                    "_source": doc
                }
                for doc in data
            ]
            helpers.bulk(self.es, workitems)
            return "ok"
        except ElasticsearchException as e:
            raise e
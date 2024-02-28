from facade.IAzure_facade import IAzureFacade
from adapters.input.Impl.Azure_adapter import AzureAdapter
from processors.Impl.Data_processor import DataProcessor
from adapters.output.Impl.Elastic_adapter import ElasticsearchCliente
import logging

class AzureFacade(IAzureFacade):
    
    def process_orchestrator(self, inputAdapter = AzureAdapter(), data_processing = DataProcessor(), elasticsearchClient = ElasticsearchCliente()):
        
        data_input = inputAdapter.get_workitems()
        
        data_process = data_processing.process_data(data_input)
        
        result = elasticsearchClient.data_index_bulk(data_process)
        logging.info("indexed data:")
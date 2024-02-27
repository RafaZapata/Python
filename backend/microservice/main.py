import logging
from facade.Impl.Azure_facade import AzureFacade

def main():
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s:%(message)s',filename='python_service.log', level=logging.INFO, datefmt='%m/%d/%Y %I:%M:%S %p')
    azure_facade = AzureFacade()
    azure_facade.process_orchestrator()

if __name__ == "__main__":
    main()
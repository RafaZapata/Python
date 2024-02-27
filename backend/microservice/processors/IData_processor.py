from abc import ABC, abstractmethod

class IDataProcessor(ABC):
    """Clase que define la interfaz IDataProcessor"""
    
    @abstractmethod
    def process_data(data):
        """
        Descripción
        -----------
            Procesa los datos de entrada de acuerdo con el modelo definido.
        """
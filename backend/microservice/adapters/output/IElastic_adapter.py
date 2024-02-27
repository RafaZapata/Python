from abc import ABC, abstractmethod

class IElasticAdapter(ABC):
    """Clase que define la interfaz IElasticAdapter"""
    
    @abstractmethod
    def data_index_bulk(self, documents):
        """
        Parametros
        ----------
        documents:
            Documentos creados de los datos obtenidos.
            
        Returns
        -------
            Indexa los datos e inserta en elasticSearch.
        """
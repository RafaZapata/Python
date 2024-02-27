from abc import ABC, abstractmethod

class ISanitizer(ABC):
    """Clase que define la interfaz ISanitize"""

    @abstractmethod
    def data_sanitizer_workitems(data):
        """
        Descripción
        -----------
            Valida la estructura de los datos obtenidos de la API.
        """
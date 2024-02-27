from abc import ABC, abstractmethod

class IAzureAdapter(ABC):
    """Clase que define la interfaz IAzureAdapter"""

    @abstractmethod
    def get_workitems(self):
        """
        Returns
        -------
            Obtiene los workitems de los proyectos de Azure.
        """
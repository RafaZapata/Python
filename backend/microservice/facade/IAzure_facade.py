from abc import ABC, abstractmethod

class IAzureFacade(ABC):
    """Clase que define la interfaz IAzureFacade"""

    @abstractmethod
    def process_orchestrator(self):
        """
        Descripción
        -----------
            Se encarga de coordinar diversas tareas y flujos de trabajo.
        """
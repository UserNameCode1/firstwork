# Importa el módulo para clases abstractas
from abc import ABC, abstractmethod

class Mob(ABC):
    """Clase abstracta base para todos los mobs."""

    def __init__(self, nombre: str, vida: int):
        self.nombre = nombre
        self.vida   = vida

    # Métodos ABSTRACTOS: cada mob DEBE implementarlos

    @abstractmethod
    def hacer_sonido(self) -> str:
        """Retorna el sonido característico del mob."""
        pass

    @abstractmethod
    def comportamiento(self) -> str:
        """Retorna 'pasivo' o 'agresivo'."""
        pass
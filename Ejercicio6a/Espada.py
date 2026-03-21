from Herramienta import Herramienta

class Espada(Herramienta):
    @property
    def nombre(self):
        return "Espada"

    def usar(self, objetivo: str) -> str:
        danio = self.calcular_danio()
        self.desgastar()
        return f"{self.nombre} de {self._material} ataca a {objetivo} (daño: {danio})"
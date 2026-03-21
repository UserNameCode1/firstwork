from Herramienta import Herramienta

class Pala(Herramienta):
    @property
    def nombre(self):
        return "Pala"

    def usar(self, objetivo: str) -> str:
        danio = self.calcular_danio()
        self.desgastar()
        return f"{self.nombre} de {self._material} excava {objetivo} (daño: {danio})"
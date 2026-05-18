from herramienta import Herramienta

class Pico(Herramienta.Herramienta):
    @property
    def nombre(self):
        return "Pico"

    def usar(self, objetivo: str) -> str:
        danio = self.calcular_danio()
        self.desgastar()
        return f"{self.nombre} de {self._material} mina {objetivo} (daño: {danio})"
class Herramienta:
    def __init__(self, material: str, durabilidad: int):
        self._material = material
        self._durabilidad = durabilidad

    def calcular_danio(self) -> int:
        # daño base puede depender del material o de la durabilidad; valor mínimo 1
        base = 5
        if self._durabilidad <= 0:
            return 0
        return max(1, base + self._durabilidad // 10)

    def desgastar(self, cantidad: int = 1):
        self._durabilidad = max(0, self._durabilidad - cantidad)


class Arco(Herramienta):
    def __init__(self, material: str, durabilidad: int, flechas: int):
        super().__init__(material, durabilidad)
        self.flechas = flechas

    @property
    def nombre(self):
        return "Arco"

    def usar(self, objetivo: str) -> str:
        if self.flechas <= 0:
            return "Sin flechas"
        
        self.flechas -= 1
        danio = self.calcular_danio()
        self.desgastar()
        return f"{self.nombre} de {self._material} dispara a {objetivo} (daño: {danio})"
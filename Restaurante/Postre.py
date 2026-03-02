
from Platillo import Platillo

class Postre(Platillo):
    def __init__(self, nombre, precio,es_sin_gluten):
        super().__init__(nombre, precio)
        self.nombre = nombre
        self.precio = nombre
        self.es_sin_gluten 


    def tipo(self):
        if self.es_sin_gluten:
            gluten = "si"
        else :
            gluten = "no"
            print(f"tipo : postre sin gluten: {gluten}")


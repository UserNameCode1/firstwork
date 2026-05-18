
from Ejercicio6.mob import Mob


class Vaca(Mob):
    def hacer_sonido(self): return "Muuuu"
    def comportamiento(self): return "pasivo"
    def moverse(self): return "Camina lentamente por el prado"
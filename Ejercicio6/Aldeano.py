class Mob:
    def hacer_sonido(self):
        pass
    def comportamiento(self):
        pass
    def moverse(self):
        pass

class Aldeano(Mob):
    def hacer_sonido(self): return "Hrmmm"
    def comportamiento(self): return "pasivo"
    def moverse(self): return "Camina buscando tradeos"
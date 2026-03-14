class Mob:
    def hacer_sonido(self):
        pass
    def comportamiento(self):
        pass
    def moverse(self):
        pass

class Creeper(Mob):
    def hacer_sonido(self): return "...Ssssss"
    def comportamiento(self): return "agresivo"
    def moverse(self): return "Corre directamente hacia el jugador"
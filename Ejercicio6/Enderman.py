class Mob:
    def hacer_sonido(self):
        pass
    def comportamiento(self):
        pass
    def moverse(self):
        pass

class Enderman(Mob):
    def hacer_sonido(self): return "Sonido distorsionado"
    def comportamiento(self): return "neutral"
    def moverse(self): return "Se teletransporta"
from Jugador import Jugador

class Observador(Jugador):
    def __init__(self, nombre: str, num_control: str, nivel: str):
        super().__init__(nombre, num_control, nivel)
        self.partidas_vistas = 0 

    def ver_partida(self):
        self.partidas_vistas += 1
        self.puntos += 5  
        
        
    def mostrar_perfil(self):
        print("\n--- Observador ---")
        super().mostrar_perfil()
        print(f"Partidas vistas: {self.partidas_vistas}")
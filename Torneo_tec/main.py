from Competidor import Competidor
from Observador import Observador

def main():
    competidor = Competidor(
        nombre="Carlos Méndez", 
        num_control="21100123", 
        nivel="avanzado", 
        equipo="Team Overflow"
    )
    competidor.mostrar_perfil()
    print() 
    
    
    competidor.ganar_puntos(50)
    competidor.perder_puntos(20)
    
   
    observador = Observador(
        nombre="Ana Torres", 
        num_control="21100456", 
        nivel="principiante"
    )
    
    
    observador.ver_partida()
    observador.ver_partida()
    
    
    observador.mostrar_perfil()

if __name__ == "__main__":
    main()
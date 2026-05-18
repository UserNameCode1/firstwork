# 1. IMPORTACIONES
from abc import ABC, abstractmethod

# 2. CONSTANTES Y CONFIGURACIÓN
DAÑO_MATERIAL = {"madera": 2, "piedra": 3, "hierro": 4, "oro": 3, "diamante": 6, "netherita": 8}

# 3. CLASES (La "fábrica")
class Herramienta(ABC):
    # ... (aquí va el código de la clase base)
    pass

class Pico(Herramienta):
    # ... (aquí va tu implementación)
    pass

# 4. EL MAIN (El "laboratorio" de pruebas)
if __name__ == "__main__":
    # Aquí creamos las instancias
    mi_pico = Pico("diamante", 5)
    
    print(f"--- Iniciando aventura con {mi_pico.nombre} ---")
    
    # Tarea 2: El bucle de uso
    while not mi_pico.rota:
        print(mi_pico.usar("bloque de obsidiana"))
        mi_pico.estado()
    
    print("¡La herramienta se ha destruido!")
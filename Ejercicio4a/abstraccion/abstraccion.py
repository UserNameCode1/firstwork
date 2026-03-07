from abc import ABC,abstractmethod

# Clase abstracta (plantilla)
class Animal(ABC):
    
    @abstractmethod
    def hablar(self):
        pass # No se implementa el metodo

class Perro(Animal):
    def hablar(self):
        print("Guau!")
    
class Gato(Animal):
    def hablar(self):
        print("Miau!")
        # Crear instancias de las clases concretas
perro = Perro() 
gato = Gato()
perro.hablar()  # Salida: Guau!
gato.hablar()   # Salida: Miau!

Animal = Animal() # Error: No se puede instanciar una clase abstracta   

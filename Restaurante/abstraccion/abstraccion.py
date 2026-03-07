from abc import ABC,abstractclassmethod

# Clase abstracta (plantilla)
class Animal(ABC):
    @abstractclassmethod
    def hablar(self):
        pass # No se implementa el metodo

class Perro(Animal):
    def hablar(self):
        print("Guau!")
    
class Gato(Animal):
    def hablar(self):
        print("Miau!")
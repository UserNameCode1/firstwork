# Ejemplo de Clases Abstractas en Python 🐍

Este repositorio contiene un ejemplo práctico sobre la implementación de **Clases Abstractas** utilizando el módulo nativo `abc` (Abstract Base Classes) de Python.

## 🚀 Descripción

El código demuestra cómo definir una estructura base (plantilla) para una jerarquía de clases. En este caso, utilizamos la clase `Animal` como base para asegurar que cualquier animal derivado implemente su propio método de comunicación.
## 🛠️ Conceptos Clave

* **`ABC`**: Clase base de la cual debe heredar cualquier clase que quiera ser abstracta.
* **`@abstractmethod`**: Decorador que indica que un método **debe** ser sobrescrito en las clases hijas.
* **Instanciación**: Una regla fundamental es que las clases abstractas no pueden ser instanciadas directamente.

## 💻 Código de Ejemplo

```python
from abc import ABC, abstractmethod

# Clase abstracta (plantilla)
class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau!")
📋 Ejecución
Al ejecutar el script, las clases concretas (Perro y Gato) funcionan correctamente, mientras que intentar crear un objeto de la clase Animal genera un error:

Python
perro = Perro()
perro.hablar() # Salida: Guau!

# Esto lanzará un TypeError:
# animal = Animal()

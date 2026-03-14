# Ejercicio 3: Simulación de Mascota Virtual 

## Introducción
Este programa implementa una clase en Python para gestionar una mascota virtual. El objetivo es practicar la lógica de estados, donde las acciones del usuario (alimentar o jugar) afectan directamente el nivel de felicidad de la mascota.

## Especificaciones del Código
- **Clase:** `Mascota`
- **Atributos:** `nombre`, `tipo`, `edad` y `nivelFelicidad` (0-100).
- **Métodos principales:**
  - `alimentar()`: Incrementa la felicidad en +10.
  - `jugar()`: Incrementa la felicidad en +20.
  - `mostrarEstado()`: Retorna un resumen del ánimo actual.
  - `esFeliz()`: Verifica si el nivel de felicidad supera los 70 puntos.

## Ejemplo de Uso
```python
mi_mascota = Mascota("Firulais", "Perro", 3, 50)
mi_mascota.jugar()
print(mi_mascota.mostrarEstado())

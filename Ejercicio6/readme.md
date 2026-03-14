# ⚒️ Práctica 3: Abstracción en POO con Python (Edición Minecraft)

¡Bienvenido al Overworld de la Programación Orientada a Objetos! Este proyecto modela diferentes criaturas (mobs) de Minecraft utilizando los conceptos fundamentales de **Clases Abstractas** y **Herencia** en Python.

## 🎯 Objetivo de Aprendizaje
El objetivo principal es aplicar la **abstracción** para definir un "contrato" base que todos los mobs deben seguir, delegando los detalles específicos (sonido, comportamiento y movimiento) a cada subclase.

---

## 🧩 Conceptos Clave Aplicados

* **ABC (Abstract Base Classes):** Uso del módulo `abc` para evitar la instanciación de la clase base.
* **@abstractmethod:** Definición de métodos obligatorios que las subclases *deben* implementar.
* **Herencia:** Las clases `Vaca`, `Creeper` y `Enderman` heredan los atributos base de `Mob`.
* **Polimorfismo:** Un mismo método (`presentarse()`) produce resultados diferentes según el objeto que lo ejecute.

---

## 💻 Estructura del Código

### La Clase Maestra: `Mob`
La clase `Mob` es abstracta. Define atributos comunes como `nombre` y `vida`, y establece tres comportamientos obligatorios:
1. `hacer_sonido()`
2. `comportamiento()`
3. `moverse()`

### Entidades Implementadas
| Mob | Sonido | Comportamiento | Movimiento |
| :--- | :--- | :--- | :--- |
| **Vaca** | Muuuu | Pasivo | Camina lento |
| **Creeper** | ...Ssssss | Agresivo | Corre al jugador |
| **Enderman** | Distorsionado | Neutral | Teletransporte |
| **Aldeano** (Bonus) | Hrmmm | Pasivo | Busca tradeos |

---

## 🚀 Ejecución y Pruebas

Para correr este proyecto, asegúrate de tener Python instalado y ejecuta:

```bash
python practica_abstraccion.py
⚠️ Notas de Implementación (Tarea 2)
Si intentas instanciar la clase base directamente:

Python
mi_mob = Mob("Test", 10)
Python lanzará un TypeError. Esto es correcto y deseado, ya que Mob es una idea abstracta y no una entidad física completa en nuestro código.

📝 Salida Esperada
El programa imprimirá fichas técnicas de cada mob en la consola, demostrando que cada uno cumple con su contrato de abstracción:

Plaintext
=== Bessie ===
❤️  Vida       : 10 HP
🔊 Sonido     : Muuuu
⚔️  Tipo       : pasivo
🏃 Movimiento : Camina lentamente por el prado

## 📖 Contexto del Problema

El sistema modela dos tipos de participantes que comparten información y comportamientos comunes (definidos en la clase base `Jugador`):
1. **Competidores:** Juegan activamente en el torneo y pertenecen a un equipo específico.
2. **Observadores:** Asisten al evento y acumulan puntos de manera automática por cada partida que ven completa.

---

## 📐 Diagrama de Clases

El diseño de clases sigue la siguiente estructura jerárquica:

* **`Jugador` (Clase Base)**
    * *Atributos:* `nombre` (str), `num_control` (str), `nivel` (str), `puntos` (int, inicia en 0).
    * *Métodos:* `ganar_puntos(cantidad)`, `perder_puntos(cantidad)`, `mostrar_perfil()`.
* **`Competidor` (Hereda de `Jugador`)**
    * *Atributos extra:* `equipo` (str).
    * *Métodos sobrescritos:* `mostrar_perfil()` (extiende el comportamiento de la clase base usando `super()`).
* **`Observador` (Hereda de `Jugador`)**
    * *Atributos extra:* `partidas_vistas` (int, inicia en 0).
    * *Métodos extra:* `ver_partida()` (suma 1 a las partidas y otorga 5 puntos automáticamente).
    * *Métodos sobrescritos:* `mostrar_perfil()` (extiende el comportamiento de la clase base usando `super()`).

---

## 📁 Estructura de Archivos

El proyecto está organizado de forma modular de la siguiente manera:

```text
torneo_tec/
│
├── Jugador.py        # Clase base con atributos comunes y lógica de puntos.
├── Competidor.py     # Clase hija que representa a los jugadores de equipos.
├── Observador.py     # Clase hija que representa a los espectadores.
└── main.py           # Archivo principal para probar el funcionamiento del sistema.

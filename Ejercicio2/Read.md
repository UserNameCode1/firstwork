# Ejercicio 2: Gestión de Cuenta Bancaria 

## Introducción
En este ejercicio se desarrolla un sistema básico para gestionar transacciones bancarias. Se enfoca en la validación de datos, asegurando que no se retiren montos superiores al saldo disponible ni se depositen valores negativos.

## Especificaciones del Código
- **Clase:** `CuentaBancaria`
- **Atributos:** `titular` y `saldo`.
- **Funcionalidades:**
  - **Depósitos:** Valida que la cantidad sea positiva.
  - **Retiros:** Verifica la disponibilidad de fondos antes de realizar la operación.
  - **Consulta:** Permite visualizar el saldo actual del titular.

## Conceptos Aplicados
- Encapsulamiento de datos.
- Lógica de control con condicionales (`if/else`).

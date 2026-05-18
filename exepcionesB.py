
print("=" * 20)



colores = ["rojo", "verde", "azul", "amarillo"]
print(f"Lista de colores: {colores} (indices 0,1,2,3)")


try:
    indice = int(input("Ingrese el índice del color que quieres acceder? (0-3): "))
    print(f"El color en el índice {indice} es: {colores[indice]}")

except ValueError as e:
    print(f" valueError: {e}")
    
except IndexError as e:
    print(f" indexError: {e}")
    print(f"Solo puedes usar los numeros 0, 1, 2 o 3 para acceder a la lista de colores.")

finally:
    print("Gracias por usar el programa.")
    
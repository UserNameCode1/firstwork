###
## exepciones basicas

# parte1 : try /except
print("=" * 20)
print("division por manejo de errores")
print("=" * 20)

try:
    a= int(input("ingrese un numero: "))
    b= int(input("ingrese otro numero: "))
    total = a / b

except ValueError:
    print("Error: Debe ingresar un número entero.")

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

else:
    print(f"El resultado de {a} dividido por {b} es: {total}")


finally:
    print("Gracias por usar el programa.")
    

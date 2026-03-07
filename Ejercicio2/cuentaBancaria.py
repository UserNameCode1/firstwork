class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito de {cantidad} realizado. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes para realizar el retiro.")
        else:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Nuevo saldo: {self.saldo}") 

    def mostrar_informacion(self):
        print(f"Titular: {self.titular}, Saldo: {self.saldo}")

        def consultar_saldo(self):
            print(f"Saldo actual: {self.saldo}")
            
            return self.saldo
        
        cuenta1 = CuentaBancaria("Carlos Aguirre", 1000)
        cuenta2 = CuentaBancaria("Maria Lopez", 500)

        print("Información de la cuenta 1:")
        cuenta1.mostrar_informacion()   
        print("Información de la cuenta 2:")
        cuenta2.mostrar_informacion()



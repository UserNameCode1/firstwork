class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
# Crear una instancia de Estudiante
estudiante1 = Estudiante("Juan Pérez", 20, "Ingeniería Informática")
# Mostrar la información del estudiante
estudiante1.mostrar_informacion()


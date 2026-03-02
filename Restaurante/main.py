from Comida import Comida
from Bebida import Bebida
from Postre import Postre

#--- OBJETOS-----------

comida1 = Comida("Tacos al pastor", 85.0,"principal")
bebida1 = Bebida("Horchata",25.0,"fria")
postre1 = ("flan",45.0, False)



 #----Mostrar--Informacion
 
comida1.mostrar_informacion()
comida1.tipo()
print("----")

bebida1.mostrar_informacion()
bebida1.tipo()
print("---")

postre1.mostar_informacion()
postre1.tipo()
print("---")


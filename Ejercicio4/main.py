from Guerrero import Guerrero
from Mago import Mago
from Arquero import Arquero


thorin = Guerrero("Thorin", 8, "Hacha")
gandalf = Mago("Gandalf", 15, "Bola de fuego")
legolas = Arquero("Legolas", 10, 30)

# 2. habilidades
thorin.presentarse()
thorin.usar_habilidad()

print("---")

gandalf.presentarse()
gandalf.usar_habilidad()

print("---")

legolas.presentarse()
legolas.usar_habilidad()
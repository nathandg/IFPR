from pneu import Pneu
from carro import Carro
from moto import Moto

# Instanciando 4 pneus

p1 = Pneu("Pirelli", "Pneu01", "Esportivo", "tam01")
p2 = Pneu("Pirelli", "Pneu02", "Esportivo", "tam02")
p3 = Pneu("Pirelli", "Pneu03", "Esportivo", "tam03")
p4 = Pneu("Pirelli", "Pneu04", "Esportivo", "tam04")

carro = Carro("Fiat", "Uno", "Branco", p1, p2, p3, p4)
moto = Moto("Honda", "CG", "Vermelha", p1, p2)

print(carro)
print(moto)
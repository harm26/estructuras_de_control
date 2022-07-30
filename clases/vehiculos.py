class Vehiculo:
    color =""
    ruedas =""
    puertas = ""

class Coche(Vehiculo):
    velocidad =""
    cilindrada = ""

coche = Coche()

coche.color = "azul"
coche.ruedas = "4"
coche.puertas = "4"
coche.velocidad = "120"
coche.cilindrada = "8"

print("Mi coche es de color "+ coche.color+", tiene "+ coche.puertas+" puertas y "+coche.ruedas+" ruedas. Su velocidad maxima es de "
      +coche.velocidad+" k/h y tiene "+coche.cilindrada+" cilindros")

from TarjetaCredito import TarjetaCredito

class Usuario:
   def __init__(self, nombre, apellido, email):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.tarjeta = TarjetaCredito(0, 20000, 0.015)
       
   def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
       self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido
       
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

miyagi.hacer_compra(150)
miyagi.hacer_compra(300)
daniel.hacer_compra(45)
print(miyagi.saldo_pagar) #Imprime: 350
print(daniel.saldo_pagar) #Imprime: 45

def metodo_ejemplo(self):

       #Llamar a los métodos de tarjeta
       self.tarjeta.compra(100)
       #Acceder a sus atributos
       print(self.tarjeta.saldo_pagar)
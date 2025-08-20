class Usuario:
    def __init__(self, nombre, apellido, email):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = 30000
       self.saldo_pagar = 0
       
    def hacer_compra(self, monto):
        self.saldo_pagar += monto
        return self
       
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

miyagi.hacer_compra(150)
miyagi.hacer_compra(300)
daniel.hacer_compra(45)
print(miyagi.saldo_pagar) #Imprime: 350
print(daniel.saldo_pagar) #Imprime: 45

miyagi.hacer_compra(1000).hacer_compra(5000)
print(miyagi.saldo_pagar) #Imprime: 6350
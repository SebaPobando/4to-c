class Pokemon:
   def __init__(self, nombre, tipo, nivel=1, salud=100, felicidad=50):
       self.nombre = nombre
       self.tipo = tipo
       self.nivel = nivel
       self.salud = salud
       self.felicidad = felicidad

   def entrenar(self):
       """Entrena al Pokémon, aumentando su nivel y felicidad, pero reduciendo su salud ligeramente."""
       pass

   def alimentar(self):
       """Aumenta la salud y felicidad del Pokémon."""
       pass

   def curar(self):
       """Cura al Pokémon, restaurando su salud, pero disminuyendo su felicidad temporalmente."""
       pass
from pokemon import Pokemon

class Entrenador:
   def __init__(self, nombre, pokemon):
       self.nombre = nombre
       self.pokemon = pokemon

   def entrenar_pokemon(self):
       """Llama al método entrenar() de la clase Pokemon."""
       pass

   def alimentar_pokemon(self):
       """Llama al método alimentar() de la clase Pokemon."""
       pass

   def curar_pokemon(self):
       """Llama al método curar() de la clase Pokemon."""
       pass

   def mostrar_info_entrenador(self):
       print (f"Entrenador: {self.nombre}")
       print (f"Pokémon: {self.pokemon.nombre}, Tipo: {self.pokemon.tipo}, Nivel: {self.pokemon.nivel}, Salud: {self.pokemon.salud}, Felicidad: {self.pokemon.felicidad}")
       """Muestra información del entrenador y su Pokémon."""
       pass
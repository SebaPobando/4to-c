from profesion import Profesion
# Creación de clase
class Persona:
    
    raza = "Humano"  # Atributo de clase
    
    def __init__(self, nombre, apellido, edad, estatura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.estatura = estatura
        self.peso = peso
        self.profesion = Profesion("Desarrollador", "Desarrolla software")  # Atributo de instancia
        
    # Métodos de clase
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} {self.apellido}.")

bastian = Persona('Bastián', 'Zumelzu', 18, 1.70, 62)
vicente = Persona('Vicente', 'Monrría', 18, 2.20, 70)

print("El nombre de mi instancia bastian, creada con la clase persona es:",bastian.nombre)
print("El apellido de mi instancia vicente, creada con la clase persona es:", vicente.apellido)

bastian.saludar()

print("La profesión de Vicente es:", vicente.profesion)
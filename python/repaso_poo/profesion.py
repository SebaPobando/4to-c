class Profesion:
    def __init__(self, nombreProfesion, descripcion):
        self.nombreProfesion = nombreProfesion
        self.descripcion = descripcion

    def __str__(self):
        return f"Profesión: {self.nombreProfesion}, Descripción: {self.descripcion}"
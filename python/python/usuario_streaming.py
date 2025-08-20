class UsuarioStreaming():
   def __init__(self, nombre, email, suscripcion="Gratis"):
       self.nombre = nombre
       self.email = email
       self.suscripcion = suscripcion
       self.lista_reproduccion = []


   def agregar_a_lista(self, titulo):
       self.lista_reproduccion.append(titulo)


   def ver_contenido(self, titulo):
       for contenido in self.lista_reproduccion:
           if contenido == titulo:
                return f"Reproduciendo: {titulo}"


   def cambiar_suscripcion(self):
       self.suscripcion = "Premium" if self.suscripcion == "Gratis" else "Gratis"
       print(f"Suscripción cambiada a: {self.suscripcion}")


   def mostrar_info_usuario(self):
       print(f"Nombre: {self.nombre}, Apellido: {self.email}, Suscripción: {self.suscripcion}, Lista de Reproducción: {self.lista_reproduccion}")
       pass
   
sebastian = UsuarioStreaming("Sebastián", "sebapoba@gmail.com")
print(sebastian.suscripcion)
sebastian.cambiar_suscripcion()
sebastian.agregar_a_lista("Breaking Bad")
sebastian.mostrar_info_usuario()
juan = UsuarioStreaming("Juan", "juanitoxxx@gmail.com")
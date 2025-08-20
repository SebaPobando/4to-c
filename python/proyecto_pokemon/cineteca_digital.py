class CinetecaDigital:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        # {id_pelicula: {"titulo": titulo, "director": director, "genero": genero, "anio": anio}}
        self.catalogo = {}  
        # {id_pelicula: nombre_usuario}
        self.peliculas_prestadas = {}  

    def agregar_pelicula(self, id_pelicula, titulo, director, genero, anio):
        """Agrega una nueva película al catálogo de la cineteca."""
        pass

    def prestar_pelicula(self, id_pelicula, usuario):
        """Registra el préstamo de una película a un usuario."""
        pass

    def devolver_pelicula(self, id_pelicula):
        """Marca una película como disponible tras ser devuelta."""
        pass

    def buscar_por_genero(self, genero):
        """Muestra las películas disponibles de un género específico."""
        pass
        
    def buscar_por_director(self, director):
        """Muestra las películas disponibles de un director específico."""
        pass

    def mostrar_catalogo_completo(self):
        """Muestra el catálogo completo con el estado de cada película."""
        pass
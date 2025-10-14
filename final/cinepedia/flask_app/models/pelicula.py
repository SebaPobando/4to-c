from flask_app.config.mysqlconnection import connectToMySQL

class Pelicula:
    def __init__(self, data):
        self.nombre_pelicula = data['nombre_pelicula']
        self.director = data['director']
        self.fecha_estreno = data['fecha_estreno']
        self.sinopsis = data['sinopsis']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM peliculas;"
        results = connectToMySQL('esquema_cinepedia').query_db(query)
        peliculas = []
        for row in results:
            peliculas.append(cls(row))
        return peliculas
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM peliculas WHERE id = %(id)s;"
        result = connectToMySQL('esquema_cinepedia').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO peliculas (nombre_pelicula, director, fecha_estreno, sinopsis, created_at, updated_at, usuario_id) VALUES (%(nombre_pelicula)s, %(director)s, %(fecha_estreno)s, %(sinopsis)s, NOW(), NOW(), %(usuario_id)s);"
        return connectToMySQL('esquema_cinepedia').query_db(query, data)
        
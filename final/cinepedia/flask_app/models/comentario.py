from flask_app.config.mysqlconnection import connectToMySQL

class Comentario:
    def __init__(self, data):
        self.contenido = data['contenido']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM comentarios;"
        results = connectToMySQL('esquema_cinepedia').query_db(query)
        comentarios = []
        for row in results:
            comentarios.append(cls(row))
        return comentarios
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM comentarios WHERE id = %(id)s;"
        result = connectToMySQL('esquema_cinepedia').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (contenido, created_at, updated_at, pelicula_id, usuario_id) VALUES (%(contenido)s NOW(), NOW(), %(pelicula_id)s, %(usuario_id)s);"
        return connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)
        
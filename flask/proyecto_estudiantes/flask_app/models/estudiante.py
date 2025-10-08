from flask_app.config.mysqlconnection import connectToMySQL

class Estudiante:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM estudiantes;"
        results = connectToMySQL('esquema_estudiantes_cursos').query_db(query)
        estudiantes = []
        for row in results:
            estudiantes.append(cls(row))
        return estudiantes
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM estudiantes WHERE id = %(id)s;"
        result = connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO estudiantes (nombre, apellido, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, NOW(), NOW());"
        return connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = "UPDATE estudiantes SET nombre = %(nombre)s, apellido = %(apellido)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM estudiantes WHERE id = %(id)s;"
        return connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.estudiante import Estudiante

class Curso:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_estudiantes_in_curso(cls, data):
        query = """
            SELECT * FROM estudiantes
            WHERE estudiantes.curso_id = %(id)s;
        """
        results = connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)
        estudiantes_en_curso = []
        for estudiante in results:
            estudiantes_en_curso.append(Estudiante(estudiante)) 
        return estudiantes_en_curso
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cursos;"
        results = connectToMySQL('esquema_estudiantes_cursos').query_db(query)
        cursos = []
        for row in results:
            cursos.append(cls(row))
        return cursos
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM cursos WHERE id = %(id)s;"
        result = connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO cursos (nombre, created_at, updated_at) VALUES (%(nombre)s, NOW(), NOW());"
        return connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)
    
    
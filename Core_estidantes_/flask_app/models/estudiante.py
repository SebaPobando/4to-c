from flask_app.config.mysqlconnection import connectToMySQL

class Estudiante:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.creted_at = data['creted_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data):
        query = "INSERT INTO estudiantes(nombre, apellido, edad, creted_at, updated_at, curso_id) VALUES (%(nombre)s, %(apellido)s, %(edad)s, NOW(), NOW(), %(curso_id)s);"
        return connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)


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
       resultado = connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)
       if len(resultado) < 1:
           return False
       return cls(resultado[0])
        
    
  
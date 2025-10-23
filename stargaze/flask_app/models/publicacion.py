from flask_app.config.mysqlconnection import connectToMySQL

class Publicacion:
    def __init__(self, data):
        self.nombre_estrella = data['nombre_estrella']
        self.fecha_encuentro = data['fecha_encuentro']
        self.lugar_encuentro = data['lugar_encuentro']
        self.descripcion = data['descripcion']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.usuario_id = data['usuario_id']
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO publicaciones (nombre_estrella, fecha_encuentro, lugar_encuentro, descripcion, created_at, updated_at, usuario_id) VALUES (%(nombre_estrella)s, %(fecha_encuentro)s, %(lugar_encuentro)s, %(descripcion)s, NOW(), NOW(), %(usuario_id)s);"
        return connectToMySQL('esquema_stargaze').query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM publicaciones;"
        results = connectToMySQL('esquema_stargaze').query_db(query)
        return results
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM publicaciones WHERE id = %(id)s;"
        results = connectToMySQL('esquema_stargaze').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def update(cls, data):
        query = """UPDATE publicaciones 
                SET nombre_estrella = %(nombre_estrella)s,
                    fecha_encuentro = %(fecha_encuentro)s,
                    lugar_encuentro = %(lugar_encuentro)s,
                    descripcion = %(descripcion)s,
                    updated_at = NOW()
                WHERE id = %(id)s;"""
        return connectToMySQL('esquema_stargaze').query_db(query, data)

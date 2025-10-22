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
        query = """
            SELECT publicaciones.*, usuarios.nombre, usuarios.apellido
            FROM publicaciones
            JOIN usuarios ON publicaciones.usuario_id = usuarios.id
            ORDER BY publicaciones.created_at DESC;
        """
        results = connectToMySQL('esquema_stargaze').query_db(query)
        
        publicaciones = []
        for row in results:
            publicacion = cls(row)
            publicacion.usuario = {
                "nombre": row['nombre'],
                "apellido": row['apellido']
            }
            publicaciones.append(publicacion)
        return publicaciones

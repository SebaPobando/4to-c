from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
   def __init__( self , data ):
       self.id = data['id']
       self.nombre = data['nombre']
       self.apellido = data['apellido']
       self.email = data['email']
       self.created_at = data['created_at']
       self.updated_at = data['updated_at']

   @classmethod
   def get_all(cls):
       query = "SELECT * FROM usuarios;"
       resultados = connectToMySQL('esquema_estudiantes_cursos').query_db(query)
       usuarios = []
       for usuario in resultados:
           usuarios.append( cls(usuario) )
       return usuarios
   
   @classmethod
   def get_by_id(cls, data):
       query = "SELECT * FROM usuarios WHERE id = %(id)s;"
       resultado = connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)
       if len(resultado) < 1:
           return False
       return cls(resultado[0])
   
   @classmethod
   def delete(cls, data):
       query = "DELETE FROM usuarios WHERE id = %(id)s;"
       return connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)
   
   @classmethod
   def update(cls, data):
       query = "UPDATE usuarios SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
       return connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)
   
   @classmethod
   def save(cls, data ):
       query = "INSERT INTO usuarios ( nombre , apellido , email , created_at, updated_at ) VALUES ( %(nombre)s , %(apellido)s , %(email)s , NOW() , NOW() );"
       return connectToMySQL('esquema_estudiantes_cursos').query_db( query, data )
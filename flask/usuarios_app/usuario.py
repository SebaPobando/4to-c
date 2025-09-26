from mysqlconnection import connectToMySQL

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
       resultados = connectToMySQL('usuarios_db').query_db(query)
       usuarios = []
       for usuario in resultados:
           usuarios.append( cls(usuario) )
       return usuarios
   
   @classmethod
   def get_by_id(cls, data):
       query = "SELECT * FROM usuarios WHERE id = %(id)s;"
       resultado = connectToMySQL('usuarios_db').query_db(query, data)
       if len(resultado) < 1:
           return False
       return cls(resultado[0])
   
   @classmethod
   def save(cls, data ):
       query = "INSERT INTO usuarios ( nombre , apellido , email , created_at, updated_at ) VALUES ( %(nombre)s , %(apellido)s , %(email)s , NOW() , NOW() );"
       return connectToMySQL('usuarios_db').query_db( query, data )
import pymysql.cursors  # Utilizamos un cursor para interactuar con BD

class MySQLConnection:
    # Clase que permite generar instancia de conexión con BD
    def __init__(self, db):
        connection = pymysql.connect(
            host='localhost',
            user='root',  # Cambia el usuario y contraseña según tu configuración
            password='root',
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        self.connection = connection  # Establecemos conexión con BD

    # Método que se encarga de ejecutar las consultas
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                executable = cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # Las consultas INSERT regresan el id del nuevo registro
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # Las consultas SELECT regresan una lista de diccionarios con los datos
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE y DELETE no regresan nada
                    self.connection.commit()
            except Exception as e:
                print("Something went wrong:", e)
                return False
            finally:
                self.connection.close()

# connectToMySQL recibe el nombre de la base de datos y genera una instancia de MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)

from flask_app import app

# ==========================================
# Importar controladores o rutas
# ==========================================
# Aquí se importan los archivos donde están definidas las rutas (controladores).
from flask_app.controllers import usuarios
from flask_app.controllers import peliculas

# Punto de entrada de la aplicación
if __name__ == "__main__":
    app.run(debug=True)

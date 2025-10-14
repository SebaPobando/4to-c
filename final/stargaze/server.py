from flask_app import app

# ==========================================
# Importar controladores o rutas
# ==========================================
# Aquí se importan los archivos donde están definidas las rutas (controladores).
# Esto asegura que Flask las registre antes de iniciar el servidor.
# Ejemplo:
#   from app.controllers import estudiantes
#   from app.controllers import cursos

# Punto de entrada de la aplicación
if __name__ == "__main__":
    # Modo debug permite reiniciar el servidor automáticamente al guardar cambios
    # y muestra mensajes de error detallados en el navegador.
    app.run(debug=True)
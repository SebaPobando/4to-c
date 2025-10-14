# ==========================================
# __init__.py
# Inicializa la aplicación Flask
# ==========================================

from flask import Flask  # Importación de Flask

app = Flask(__name__)  # Crea instancia de Flask

app.secret_key = "clave secreta, shhhh!"  # Clave para manejar sesiones y formularios
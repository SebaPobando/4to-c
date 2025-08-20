from flask import Flask, render_template

app = Flask(__name__)

# Datos de jugadores con puntajes
jugadores = [
   {"nombre": "AlexGamer", "puntaje": 5000},
   {"nombre": "PixelMaster", "puntaje": 7500},
   {"nombre": "ShadowNinja", "puntaje": 8200},
   {"nombre": "CyberWarrior", "puntaje": 9100},
   {"nombre": "UltraNoob", "puntaje": 3000}
]


# Ruta para mostrar el ranking de jugadores
@app.route("/")
def ranking():
    return render_template("index.html", jugadores=jugadores)

# Ruta para mostrar un número limitado de jugadores
@app.route("/ranking/<int:numero>")
def ranking_jugadores(numero):
    jugadores_filtrados = jugadores[:numero] if numero <= len(jugadores) else jugadores
    return render_template("index.html", jugadores=jugadores_filtrados)

# Ruta para personalizar el color del ranking
@app.route("/ranking/<int:numero>/<string:color>")
def ranking_color(numero, color):
    jugadores_filtrados = jugadores[:numero] if numero <= len(jugadores) else jugadores
    return render_template("index.html", jugadores=jugadores_filtrados, color=color)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "⚠️ ¡Sobrecarga de rutas! No encontramos a dónde quieres ir, inténtalo de nuevo.", 404

# Ejecutar el servidor
if __name__ == "__main__":
   app.run(debug=True)
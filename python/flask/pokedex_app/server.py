from flask import Flask, render_template

app = Flask(__name__)

# Base de datos ficticia de Pokémon
pokedex = [
   {"id": 1, "nombre": "Bulbasaur", "tipo": "Planta/Veneno", "imagen": "bulbasaur.png", "poder": 45, "altura": "0.7m", "peso": "6.9kg"},
   {"id": 4, "nombre": "Charmander", "tipo": "Fuego", "imagen": "charmander.png", "poder": 39, "altura": "0.6m", "peso": "8.5kg"},
   {"id": 7, "nombre": "Squirtle", "tipo": "Agua", "imagen": "squirtle.png", "poder": 44, "altura": "0.5m", "peso": "9.0kg"},
   {"id": 25, "nombre": "Pikachu", "tipo": "Eléctrico", "imagen": "pikachu.png", "poder": 35, "altura": "0.4m", "peso": "6.0kg"},
   {"id": 39, "nombre": "Jigglypuff", "tipo": "Normal/Hada", "imagen": "jigglypuff.png", "poder": 115, "altura": "0.5m", "peso": "5.5kg"},
   {"id": 52, "nombre": "Meowth", "tipo": "Normal", "imagen": "meowth.png", "poder": 40, "altura": "0.4m", "peso": "4.2kg"},
   {"id": 54, "nombre": "Psyduck", "tipo": "Agua", "imagen": "psyduck.png", "poder": 50, "altura": "0.8m", "peso": "19.6kg"},
   {"id": 94, "nombre": "Gengar", "tipo": "Fantasma/Veneno", "imagen": "gengar.png", "poder": 60, "altura": "1.5m", "peso": "40.5kg"},
   {"id": 95, "nombre": "Onix", "tipo": "Roca/Tierra", "imagen": "onix.png", "poder": 35, "altura": "8.8m", "peso": "210.0kg"},
   {"id": 143, "nombre": "Snorlax", "tipo": "Normal", "imagen": "snorlax.png", "poder": 160, "altura": "2.1m", "peso": "460.0kg"}
]

# Ruta principal
@app.route("/")
def home():
   return render_template("index.html")

# Ruta para mostrar todos los Pokémon
@app.route("/pokemon")
def mostrar_todos_los_pokemon():
   return render_template("pokemon.html", pokedex=pokedex)

# Ruta para mostrar un Pokémon por nombre
@app.route("/pokemon/<string:nombre>")
def mostrar_pokemon_por_nombre(nombre):
   pokemon = next((p for p in pokedex if p["nombre"].lower() == nombre.lower()), None)
   if pokemon:
       return render_template("pokemon.html", pokedex=[pokemon])
   else:
       return render_template("404.html", mensaje="Pokémon no encontrado"), 404

# Ruta para mostrar un Pokémon por número en la Pokédex

@app.route("/pokemon/<int:id>")
def mostrar_pokemon_por_id(id):
   pokemon = next((p for p in pokedex if p["id"] == id), None)
   if pokemon:
       return render_template("pokemon.html", pokedex=[pokemon])
   else:
       return render_template("404.html", mensaje="Pokémon no encontrado"), 404

# Ruta para mostrar una cantidad específica de Pokémon
@app.route("/pokemon/cantidad/<int:cantidad>")
def mostrar_cantidad_de_pokemon(cantidad):
   return render_template("pokemon.html", pokedex=pokedex[:cantidad])

# Ruta de error cuando no se encuentra un Pokémon
@app.errorhandler(404)
def pagina_no_encontrada(e):
   return render_template("404.html", mensaje="Página no encontrada"), 404

if __name__ == "__main__":
   app.run(debug=True)
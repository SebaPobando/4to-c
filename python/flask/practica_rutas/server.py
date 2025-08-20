from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '🌎 ¡Bienvenido a nuestro servidor Flask!'

@app.route('/explorar')
def explorar():
    return '🔍 ¿Qué ruta estás buscando? ¡Prueba con diferentes direcciones!'

@app.route('/perfil/<nombre>')
def perfil(nombre):
    return f'👤 Bienvenid@ {nombre} a tu perfil personalizado en nuestra app.'

@app.route('/repite/<int:veces>/<mensaje>')
def mensaje(veces, mensaje):
    return '🔄 Repite después de mí: ' + f'{mensaje}'*veces

if __name__ == "__main__":
   app.run(debug=True)
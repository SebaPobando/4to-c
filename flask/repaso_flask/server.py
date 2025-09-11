from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', nombre = 'Mundo', cantidad = 5)

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f'Hola, {nombre}'

@app.route('/saludo/<nombre>/<int:edad>')
def saludo_con_edad(nombre, edad):
    return f'Hola, {nombre}. Tienes {edad} años.'


if __name__ == "__main__":
    app.run(debug=True)
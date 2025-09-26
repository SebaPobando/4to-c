from flask import Flask, render_template, redirect, request
from usuario import Usuario

app = Flask(__name__)

@app.route("/")
def index():
   usuarios = Usuario.get_all()
   print(usuarios)
   return render_template("index.html", todos_usuarios = usuarios)

@app.route("/nuevo")
def nuevo():
   usuarios = Usuario.get_all()
   return render_template("mostrar_usuarios.html", todos_usuarios=usuarios)

@app.route("/crear_usuario", methods=['POST'])
def crear_usuario():
   datos = {
       "nombre": request.form['nombre'],
       "apellido": request.form['apellido'],
       "email": request.form['email']
   }
   Usuario.save(datos)
   return redirect('/nuevo')

@app.route("/usuario/<int:id>")
def ver_usuario(id):
   data = { "id": id }
   usuario = Usuario.get_by_id(data)
   return render_template("mostrar_uno.html", un_usuario=usuario)
    
if __name__ == "__main__":
    app.run(debug=True)
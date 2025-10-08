from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.usuario import Usuario

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

@app.route("/usuario/eliminar/<int:id>")
def borrar_usuario(id):
   data = { "id": id }
   Usuario.delete(data)
   return redirect('/nuevo')

@app.route("/usuario/actualizar/<int:id>", methods=['POST'])
def actualizar_usuario(id):
    datos = {
        "id": id,
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email']
    }
    Usuario.update(datos)
    return redirect('/nuevo')
 
@app.route("/usuario/editar/<int:id>")
def cargar_editar(id):
    data = { "id": id }
    usuario = Usuario.get_by_id(data)
    print(usuario)
    return render_template("editar.html", un_usuario=usuario)
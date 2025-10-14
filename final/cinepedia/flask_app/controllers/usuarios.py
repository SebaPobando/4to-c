from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.usuario import Usuario
from flask_app.models import pelicula
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def cargar_dashboard():
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión para poder acceder al dashboard.")
        return redirect('/')
    datos = {"id": session['usuario_id']}
    usuario = Usuario.get_by_id(datos)
    peliculas = pelicula.Pelicula.get_all()
    return render_template('dashboard.html', usuario = usuario, peliculas = peliculas)

@app.route('/registrar', methods=['POST'])
def registrar():
    password_hasheada = bcrypt.generate_password_hash(request.form['password'])
    datos = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "password": password_hasheada
    }

    usuario_id = Usuario.save(datos)

    session['usuario_id'] = usuario_id
    session['nombre'] = request.form['nombre']

    return redirect('/dashboard')  

@app.route('/cerrar')
def cerrar():
    session.clear()
    flash("Has cerrado sesión correctamente", "success")
    return redirect('/')
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    if request.method == 'POST':
        password_hash = bcrypt.generate_password_hash(request.form['password'])
        datos = {
            'nombre': request.form['nombre'],
            'apellido': request.form['apellido'],
            'email': request.form['email'],
            'password': password_hash
        }
        usuario_id = Usuario.save(datos)
        if usuario_id:
            session['usuario_id'] = usuario_id
            return redirect('/dashboard')
        else:
            flash("Error al guardar el usuario", "error")
            return redirect('/')
    return render_template('index.html')


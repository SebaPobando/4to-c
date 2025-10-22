from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    
    password_hasheada = bcrypt.generate_password_hash(request.form['password'])
    
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "password": password_hasheada
    }
    usuario_id = Usuario.save(data)
    session['usuario_id'] = usuario_id
    
    # Revisamos que los datos se estén guardando
    print("Usuario registrado con ID:", usuario_id)
    print(request.form)
    
    return redirect('/dashboard')

from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.publicacion import Publicacion

@app.route('/dashboard')
def dashboard():
    publicaciones = Publicacion.get_all()
    return render_template('publicaciones.html', publicaciones = publicaciones)

@app.route('/nueva_publicacion', methods=['POST'])
def nueva_publicacion():
    data = {
        "nombre_estrella": request.form['nombre_estrella'],
        "fecha_encuentro": request.form['fecha_encuentro'],
        "lugar_encuentro": request.form['lugar_encuentro'],
        "descripcion": request.form['descripcion'],
        "usuario_id": session['usuario_id']
    }
    Publicacion.save(data)
    print(request.form)
    return redirect('/dashboard')

@app.route('/editar/<int:id>')
def editar(id):
    data = {
        "id": id
    }
    publicacion = Publicacion.get_by_id(data)
    return render_template('editar.html', publicacion=publicacion)

@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    data = {
        "id": id,
        "nombre_estrella": request.form['nombre_estrella'],
        "fecha_encuentro": request.form['fecha_encuentro'],
        "lugar_encuentro": request.form['lugar_encuentro'],
        "descripcion": request.form['descripcion']
    }
    Publicacion.update(data)
    return redirect('/dashboard')
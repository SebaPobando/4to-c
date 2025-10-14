from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.pelicula import Pelicula

@app.route('/cine')
def cine():
    return render_template('nueva_pelicula.html')


@app.route('/pelicula/agregar', methods=['POST'])
def agregarPelicula():
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión para agregar películas")
        return redirect('/login')
    
    datos_pelicula = {
        "nombre_pelicula": request.form['nombre_pelicula'],
        "director": request.form['director'],
        "fecha_estreno": request.form['fecha_estreno'],
        "sinopsis": request.form['sinopsis'],
        "usuario_id": session['usuario_id']
    }

    Pelicula.save(datos_pelicula)

    flash("Película agregada correctamente")
    return redirect('/dashboard')

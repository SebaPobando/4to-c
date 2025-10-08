from flask_app import app #Importamos la app
from flask import render_template,redirect,request,session,flash
from flask_app.models.estudiante import Estudiante #Importamos la clase
from flask_app.models.curso import Curso #Importamos la clase

@app.route('/estudiante')
def estudiante():
    cursos = Curso.get_all()
    return render_template('estudiantes.html', cursos = cursos)

@app.route('/crear_estudiante',methods=['POST'])
def crear_estudiante():
    datos = {
        "nombre":request.form['nombre'],
        "apellido":request.form['apellido'],
        "edad": request.form['edad'],
        "curso_id": request.form['curso_id']
    }
    Estudiante.save(datos)  
    return redirect('/')
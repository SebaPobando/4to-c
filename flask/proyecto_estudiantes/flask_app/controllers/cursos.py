from flask_app import app #Importamos la app
from flask import render_template,redirect,request,session,flash
from flask_app.models.curso import Curso #Importamos la clase
from flask_app.models.estudiante import Estudiante #Importamos la clase

@app.route('/')
def index():
    cursos = Curso.get_all()
    estudiantes = Estudiante.get_all()
    return render_template('cursos.html', cursos = cursos, estudiantes = estudiantes)

@app.route('/crear_curso',methods=['POST'])
def crear_curso():
    datos = {
        "nombre":request.form['nombre']
    }
    Curso.save(datos)
    return redirect('/')

@app.route('/cursos/<int:curso_id>')
def estudiantes_en_curso(curso_id):
    data = {'id': curso_id}
    estudiantes = Curso.get_estudiantes_in_curso(data)
    return render_template('tabla_estudiantes.html', estudiantes=estudiantes)


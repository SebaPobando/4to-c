from flask import Flask 

app = Flask(__name__) 

@app.route('/') 
def hola_flask():
   return '¡Hola Flask!' 

@app.route('/exito')
def exito(): 
   return "¡Éxito!" 

@app.route('/nigga')
def nigga():
   return '🐵'

@app.route('/saludo/<nombre>')
def saludo(nombre):
   print(nombre)
   return (f'¡Hola {nombre}!')

@app.route('/color/<nombre>/<color>')
def color_favorito(nombre, color):
   print(nombre)
   print(color)
   return f'Hola {nombre}, tu color favorito es el {color}'

@app.route('/saludo/<nombre>/<int:num>')
def hola_cantidad(nombre, num):
   return f'¡Hola {nombre}!'*num

if __name__=="__main__":  
   app.run(debug=True)   
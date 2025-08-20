diccionario_vacio = {}

persona = {
    'nombre': 'Carmen', 
    'edad': 31, 
    'altura': 1.71, 
    'usa_lentes': False}

persona['nombre'] = 'Valeria'  # Actualiza si el valor de la llave existente

persona['hobbies'] = ['jugar videojuegos', 'programación'] 

# Agrega esa clave-valor si no existía previamente

print(persona)

# Imprime: {'nombre': 'Carmen', 'edad': 31, 'altura': 1.71, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']}

altura = persona.pop('altura')  # Elimina la clave indicada y devuelve el valor

print(altura)    # Imprime: 1.71

print(persona) 

# salida: {'nombre': 'Carmen', 'edad': 31, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']} 

print(type(3.1416)) #Imprime: <class 'float'>

print(type(persona)) #Imprime <class 'dict'>
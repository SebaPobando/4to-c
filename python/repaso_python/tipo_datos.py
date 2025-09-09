# Datos Booleanos
mayor_edad = False
mujeres_curso = True
# Nos sirve para verificar si algo es verdadero o falso

# Datos Numéricos
edad = 25  # Entero
altura = 1.75  # Decimal (float)
# Nos sirve para representar cantidades y realizar cálculos matemáticos

# Datos de Texto
nombre = "Juan"
apellido = "Pérez"
nombre_completo = "Juan Pérez asakjdñglakjsgd"
# Nos sirve para representar palabras, frases o cualquier tipo de información textual

# Listas
# Lista Vacía
lista_vacia = []
# Lista con Datos
gatos = ["Shizuku", "Lily", "Wilson"]
print(gatos[1])  # Acceder al segundo elemento de la lista
# Agregar un elemento a la lista
gatos.append("Ging")
# Volver a imprimir la lista para ver el cambio
print(gatos)
# Eliminar dato de la lista
gatos.pop()  # Elimina el último elemento
print(gatos)
# Eliminar un gato eligiendo posición
gatos.pop(0)  # Elimina el primer elemento
print(gatos)

# Tuplas
# Tupla Vacía
tupla_vacia = ()
# Tupla con Datos
colores = ("Rojo", "Verde", "Azul")
# Intentar modificar un dato de la tupla (esto generará un error)
# colores[0] = "Morado"
print(colores)

# Diccionarios
# Diccionario Vacío
diccionario_vacio = {}
# Diccionario con Datos
hamburguesa = {
    "nombre": "Hamburguesa Vaquera",
    "precio": "$1000",
    "ingredientes": ["Carne de vacuno", "Queso cheddar", "Tocino", "Lechuga", "Tomate", "Cebolla"],
    "lleva_bebida": True,
    "lleva_papas": True,
    "pertenece_promocion": False
}
# Acceder a un valor del diccionario
print("Los ingredientes de la  hamburguesa vaquera son: ", hamburguesa["ingredientes"])

# Modificar un valor del diccionario
hamburguesa["precio"] = "$2000"
print("El nuevo precio de la hamburguesa vaquera es: ", hamburguesa["precio"])
# Agregar un nuevo par clave-valor al diccionario
hamburguesa["tamaño"] = "Grande"
print("El tamaño de la hamburguesa es: ", hamburguesa["tamaño"])
print(hamburguesa)

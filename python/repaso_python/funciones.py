def multiplicacion(a, b):
    resultado = a * b
    return resultado

multiplicacioUno = multiplicacion(5, 12)
print(multiplicacioUno)
# print(multiplicacion(5, 12))

# Parámetros y argumentos
def buenos_dias(nombre = "Rodrigo"):
    print (f"¡Buenos días, {nombre}!")

buenos_dias("Bastian")
buenos_dias("Francisco")
buenos_dias()
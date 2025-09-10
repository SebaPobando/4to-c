# Bucle con rango final
for i in range(10):
    pass
    
# Bucle con rango inicial y final
for i in range(5, 15):
    pass
    
# Bucle con rango inicial, final y paso
for i in range(0, 30, 5):
    pass

# Bucle que recorre un string
for letra in 'Python':
   pass

#Bucle que recorre una lista
frutas = ["Manzana", "Banana", "Cereza"]
for fruta in frutas:
    pass
    
# Bucle que recorre un diccionario e imprime la clave
estudiante = {
    "nombre": "Gonzalo", 
    "curso": "Python"
    }

for clave in estudiante:
   print(clave)
#Imprime: nombre, curso

# Bucle que recorre un diccionario e imprime el valor
for clave in estudiante:
    print(estudiante[clave])
    

# Bucles While
numero = 0
while numero <= 10:
    print(numero)
    numero += 1
else:
    print("El número es mayor que 10")
    
# Control de bucles
for letra in "detente":
   if letra == "n":
       break
   print(letra)
   
# Bucle con continue
for letra in "detente":
   if letra == "n":
        continue
   print(letra)
#Imprime: d, e, t, e, t, e
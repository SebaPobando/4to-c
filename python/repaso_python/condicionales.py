# Condicional simple
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Condicional múltiple
numero = 20
if numero > 20:
    print("El número es mayor que 20")
elif numero == 20:
    print("El número es igual a 20")
elif numero < 4:
    print("El número es menor que 4")
else :
    print("El número está entre 5 y 20")

# # Operadores comparativos
# a == b # a es igual a b
# a != b # a es diferente a b
# a > b  # a es mayor que b
# a < b  # a es menor que b
# a >= b # a es mayor o igual que b
# a <= b # a es menor o igual que b

numeroUno = 20
numeroDos = 30

# Operador AND
if numeroUno == 20 and numeroDos == 30:
    print("Ambas condiciones son verdaderas")
else:
    print("Al menos una de las condiciones es falsa")
    
# Operador OR
if numeroUno == 20 or numeroDos == 10:
    print("Al menos una de las condiciones es verdadera")
else:
    print("Ninguna condición es verdadera")



'''
Lo primero que vamos a realizar es dar la bienvenida 
preguntando un número entre 1 y 1000

Cuando el usuario proporciona el número, comprobaremos si es par o impar 
y después imprimimos el mensaje con el resultado.
'''

# Entrada (Número de 1 - 1000)
# Comprobación de si es par o impar
# Imprimimos el número ingresado y si es par o impar

while True:
    number= int(input("Ingrese un número del 1 - 1000: "))
    if (number % 2 == 0):
        print(f"El número {number} es par")
    else:
        print(f"El número {number} es impar")
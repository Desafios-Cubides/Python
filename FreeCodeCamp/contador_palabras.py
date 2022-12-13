"""
Preguntamos al usuario en que está pensando. Cuando se introduce la 
respuesta, realizará el conteo de palabras en la sentencia e imprimimos en la 
salida el resultado.

Ejemplo:

Pregunta: ¿En qué estás pensando?

Entrada: Bien, hoy es el día en el que me voy a crear un desarrollador experto

Salida: ¡Muy bien, tu me has mostrado tu pensamiento en 15 palabras!

Para llevar esto a cabo, vamos a crear un fichero de texto y añadimos una unas 
frases, y contamos cuántas palabras tiene y lo imprimimos.
"""

import os


file= open("/home/aaa00/Documentos/Programación/Python/00 Ficheros/first.txt", "w") # Abrimos en modo escritura
file.write(input("Ingresa tus pensamientos: ")  + os.linesep) 
# os.linesep nos ayuda a completar los espacios necesario para hacer un salto de linea en la consola

"""
Obte por volver hacer uso de la var file pero con el parametro rt para lectura, ya que
no se como se incluye directamente en una sola linea con w
"""

file= open("/home/aaa00/Documentos/Programación/Python/00 Ficheros/first.txt", "rt") # Abrimos en modo lectura
contador= file.read()
palabras= contador.split() # Se divide el string en substring dentro de un vector

# se cuenta la cantidad de strings dentro de la var(palabras) porque ahora se trata como un conjunto de substrings dentro de un vector
# Vealo como contar cuantos elementos hay en dicha estructura de datos
print(f'El número de palabras dígitadas son: {len(palabras)}') 
file.close()


# Algoritmo simplificado para leer cantidad de palabras
a= input("Ingresa cuáles son tus pensamientos: ")
plabras= a.split()
print(len(plabras))


"""
Pedimos al usuario que introduzca varias entradas con varias preguntas.

Puede ser cualquier cosa, como un nombre, un adjetivo, un pronombre o 
incluso una acción. Una vez que se obtiene la entrada, se puede 
reorganizar para construir su propia historia.
"""

# Entrada (nombre, adjetivo, pronombre, acción)
# Se puede reorganizar para construir su propia historia.
# Salida (Historia con las palabras ingresadas)

""" Mi Code
name= input("Ingrese un nombre: ")
adj= input("Ingrese un adjetivo: ")
pron= input("Ingrese un pronombre: ")
verb= input("Ingrese un acción: ")


history= f'''
        Erase una vez una persona llamada {name} un {adj},
        esta decia todos los días {pron} {verb}.
        '''

print(history)
"""

# https://gist.github.com/mugan86/84dbe28a60060720ec86d03e963675d5 (mugan86)

loop= 1

while (loop < 10):

    # Pedir (Entradas)
    noun= input("Ingrese un sustantivo: ")
    name= input("Ingrese un nombre: ")
    adjetive= input("Ingrese un adjetivo: ")
    adjetive2= input("Ingrese un adjetivo plural: ")
    pronomb= input("Ingrese un pronombre exepto ('Yo'): ")
    verb= input("Ingrese un verbo: ")

    # Historias
    print("-------------------------")
    print(f"Cuando {name} {verb} se logra apreciar que es {adjetive}")
    print(f"los gatos son {adjetive2} según Wakopodia")
    print(f"Yo ví cuando se compraron l@s {noun} y eran {adjetive2}")
    print(f"Al {verb} {pronomb} se ve(n) {adjetive2}")
    print("--------------------------")


    loop += 1

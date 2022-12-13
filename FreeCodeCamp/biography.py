""" Formulación del problema
Pregunte a un usuario su información personal en una sola ronda de 
preguntas. Luego hay que verificar que la información que se ha 
ingresado sea válida. Finalmente, se imprime un resumen de toda la 
información que ha sido ingresada.

Por ejemplo: ¿Cuál es su nombre? Si el usuario ingresa *, hay que indicar que 
la entrada es incorrecta y se pide que se ingrese correctamente un nombre válido.

Cuando se introduce todo correctamente, se muestra un resumen como el que 
aparece a continuación:

- Nombre: John Doe
- Fecha de nacimiento: Jan 1, 1954
- Dirección: 24 fifth Ave, NY
- Metas personales: To be the best programmer there ever was.
"""

# Se crea una base de datos
biography= {"name":"Juan", "born":"01 OCTUBRE 2001", "Dire":"Kra 150", "Meta":"Ingeniero y Empresario"}


""" First Option
Name= input("Join you first name: ")
Born= input("Join you born [DD/MM/AA]: ")
Dire= input("Join you Diretion: ")
Meta= input("Join you Dreams: ")


# Se hace una comparación con la inf ingresada y la base de datos
if (biography["name"] == Name and biography["born"] == Born and biography["Dire"] == Dire and biography["Meta"] == Meta):
    print(f"Nombre: {Name}")
    print(f"Fecha nacimiento: {Born}")
    print(f"Dirección: {Dire}")
    print(f"Sueños: {Meta}")
else: # Si algun dato ingresado no es correcto se imprime el mensaje
    print("Datos Erroneos")
"""    

""" Second Option
condicion= True # Valor para loop (While)

def datos(Name, Born, Dire, Meta):
# Se compara cada valor de los parametros para asì imprimir su resultado si es correcto
# En caso contrario se imprimira un mensaje de error correspondiente a dicho dato

    if (biography["name"] == Name):
        print(f"Nombre: {Name}")
        a= True
    else:
        print("Nombre erroneo o mal digitado [Ex: Marcos]")
        a= False
    if (biography["born"] == Born):
        print(f"Fecha de nacimiento {Born}")
        b= True
    else:
        print("Fecha de nacimiento erronea")
        b= False
    if (biography["Dire"] == Dire):
        print(f"Dirección: {Dire}")
        c= True
    else:
        print("Dirección erronea")
        c= False
    if (biography["Meta"] == Meta):
        print(f"Objetivos: {Meta}")
        d= True
    else:
        print("Objetivo incorrecto")
        d= False

    print("________________________________") # División visual por consola
    # Si la condición anterior fue correcta las variables de retorno serán (True) o si no (False)
    return a, b, c, d 


while condicion == True:

    Name= input("Join you first name: ")
    Born= input("Join you born [DD/MM/AA]: ")
    Dire= input("Join you Diretion: ")
    Meta= input("Join you Dreams: ")

    print("________________________________")

    # Lamaremos a la función (datos) e ingresaremos la inf ingresada en ella
    # Se guardara el retorno en la variable para luego compararla
    bu= datos(Name, Born, Dire, Meta)

    # Si la variable (bu) es igual al set, entonce la var (condición) cambia su valor para salir de (while)
    if (bu == (True, True, True, True)):
        condicion= False
""" 

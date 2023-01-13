''' Link (https://py.checkio.org/en/mission/sum-numbers/)
'''
'''
def sum_number(text):
    """Esta función nos ayuda a sumar
    dos números que estan dentro de un String
    ingresado por el usuario"""

    mensaje = text.split()
    nums = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5,
            "6":0, "7":7, "8":8, "9":9}
    sum = 0

    for i in mensaje: # Recorremo cada posición de la lista
        count = 0

        for j in i: # Recorremos cada carácter
            
            if (j in nums):
                count += 1

        if (count == len(i)): # Si la longitud corresponde sumamos
            sum += int(i)

    print(sum)
'''

def sum_number(text):
    ''''''
    mensaje = text.split()
    sum = 0

    for i in mensaje:
        if (i.isdigit()):
            sum += int(i)

    return sum


mensaje = input("Ingrese un mensaje: ")
print(sum_number(mensaje))
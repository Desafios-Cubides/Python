def binario(decimal): #Solo funciona con números positivo enteros
    binario= ""
    while decimal // 2 != 0:
        binario= str(decimal % 2 ) + binario
        decimal= decimal // 2
    return str(decimal) + binario


numero= int(input("Ingrese un número para convertir a BINARIO: "))
print(binario(numero))
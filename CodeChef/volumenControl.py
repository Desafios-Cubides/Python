cPrueba= int(input())

for i in range(0, cPrueba):
    inputData= input()

    # Cada String se agrega a un vector
    # Cada data del vector se convierte en Int
    contenedor= inputData.split()
    X= int(contenedor[0])
    Y= int(contenedor[1])

    # Se hace una comparación de valores para
    # Luego imprimir la diferencia
    if(X < Y):
        print(Y - X)
    elif(X > Y):
        print(X - Y)
    else:
        print(X - Y)
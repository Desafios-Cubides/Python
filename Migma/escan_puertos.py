import sys
import socket

objetivo= socket.gethostbyname(input("Ingrese su dirección ip: "))
print("Escaneando objetivo: " + objetivo)


try:
    for port in range(1, 150):
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultado= s.connect_ex((objetivo, port))
        if resultado == 0:
            print(f"El puerto {port} esta abierto")
        s.close()
except:
    print("\n Saliendo...") #Ctrl + c
    sys.exit(0)
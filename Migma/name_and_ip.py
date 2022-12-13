import socket

hostname= socket.gethostname() #Obtenemos el nombre del host
ip= socket.gethostbyname(hostname) #Obtenemos el ip del host

print(f"El nombre de tú pc es: {hostname} y tú ip es: {ip}")
import socket 
#Objeto socket con protocolo TCP de tipo internet AF_INET 
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Lugar a donde nos vamos a conectar, recomendado un puerto mayor a 100
client_socket.connect(('localhost',555))
#Que vamos a enviar, debe ser codificado
client_socket.send('Usuario uno reportandose'.encode())
#client_socket.close()
#Para cerrar puerto de forma segura es: client_socket.close()
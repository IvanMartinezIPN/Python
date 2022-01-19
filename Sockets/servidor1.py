import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#lanzar servidor
server_socket.bind(('localhost',555))
#escuchar peticiones de clientes y el numero de conexiones
server_socket.listen(2)

while True:
    #objetos para aceptar peticion
    connection, addres = server_socket.accept()
    #Almacenamiento de mensaje
    buffer = connection.recv(64)
    if len(buffer)> 0:
        print('\nMensaje entrante:')
        print(buffer)
        print('Gracias por reportarse')
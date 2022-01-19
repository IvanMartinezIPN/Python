import smtplib  #biblioteca para transferencia SMPT
import getpass #Ocultar la entrada

host_server = "smtp.gmail.com" #Direccion de host
port = 587 #Puerto que requiere TLS

remit = "tareasydesarrollo@gmail.com" #cuenta a usar
rem_pswd = getpass.getpass('Password: ')#password de cuenta

message = ' Hola este es un mensaje de prueba'

#iniciando conexion con host y puerto

serv_connect = smtplib.SMTP(host_server,port)
serv_connect.ehlo()#Nos identifica ante el servidor

serv_connect.starttls()#Genera una encriptacion TLS, que es la que requiere el puerto

#ingresando credenciales
serv_connect.login(user= remit, password= rem_pswd)

#enviar correo a traves del servidor
serv_connect.sendmail(remit,"jose.ivan.martinez.alvarado@gmail.com",message)

#nos desconectamos del servidor
serv_connect.quit()
print('El envio de correo fue exitoso')
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart #Configurar partes del correo como subjetc, from ,to
from email.mime.image import MIMEImage #Para agregar imagenes
from email.mime.text import MIMEText #Objetos de tipo texto

#definir datos
remit = "tareasydesarrollo@gmail.com" #cuenta a usar
rem_pswd = getpass.getpass('Password: ')#password de cuenta
destinatarios = ["andypruebaa@gmail.com",
"smto.cesar@gmail.com",
"ericka.pereda99@gmail.com",
"ev.persal@gmail.com",
"rodriguezgranados.carlosignacio@gmail.com",
"protecossilvestre@gmail.com",
"awadeburritos@gmail.com",
"alextools2022@gmail.com",
"phyto.soka7@gmail.com",
"kalebpascoepru@gmail.com",
"graphycrypto8@gmail.com",
"esnarftan75@gmail.com",
"tareasydesarrollo@gmail.com",
"ov61646@gmail.com",
"mirisosa300899@gmail.com",
"lcarrenovelazquez@gmail.com",
"ascgv0612@gmail.com",
"ipp867992@gmail.com",
"diegoviv817@gmail.com"
]

#definir nuestra conexion al servidor
servidor = smtplib.SMTP('smtp.gmail.com',587)
servidor.starttls() #iniciamos TLS
servidor.login(remit, rem_pswd)#credenciales

asunto = 'Bodorrio'
contenido_msg = ' Informacion adicional\n '

for email in destinatarios: #Enviar correos
    mensaje = MIMEMultipart()
    #COLOCANDO LOS PARAMETROS DEL MENSAJE 
    mensaje['From'] = 'DIANA Y EL ARGENTINO'
    mensaje['To'] = email
    mensaje['Subject'] = asunto

    #agregar el texto
    mensaje.attach(MIMEText(contenido_msg,'plain'))
    #agregar la imagen
    mensaje.attach(MIMEImage(open('meme.png','rb').read(),name = 'Meme.png'))
    #rb read binary
    #enviar correo
    servidor.sendmail(remit,email,mensaje.as_string()) 
    #como mensaje es una instancia de Multipart lo pasamos a string 
    print('Los correos se enviaron adecuadamente a: {}'.format(email))

#desconexion
servidor.quit()




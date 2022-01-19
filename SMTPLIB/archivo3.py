import smtplib
import getpass
from email.mime.multipart import MIMEMultipart #Configurar partes del correo como Subject, From, To
from email.mime.image import MIMEImage # Para agregar imagenes
from email.mime.text import MIMEText # Para objetos de tipo texto

# Definir remitente, contraseña y destinatarios
remitente = "tareasydesarrollo@gmail.com"
rem_pswd = getpass.getpass("Contraseña: ")
destinarios = ["andypruebaa@gmail.com",
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
"diegoviv817@gmail.com"]

# Definir nuestra conexion al servidor
servidor = smtplib.SMTP("smtp.gmail.com",587)
servidor.starttls() # Iniciamos encriptacion TLS
servidor.login(remitente,rem_pswd) # Ingreso con credenciales

asunto = "Bodorrio"
contenido_msg = "Hola, te traigo ofertas y modelos que no vas a poder rechazar, unete ahora mismo.\n\nEso es todo el mensaje, adios"

for email in destinarios: # Enviando correos
	# Generando instancia MIMEMultipart
	mensaje = MIMEMultipart() # Una instancia de clase

	# Colocando los parametros del mensaje
	mensaje["From"] = "Diana y el Argentino"
	mensaje["To"] = email
	mensaje["Subject"] = asunto

	# Agregar el texto
	mensaje.attach(MIMEText(contenido_msg,'plain'))
	# Agregar la imagen
	mensaje.attach(MIMEImage(open("meme.png","rb").read(), name = "meme.png"))

	# Enviar el correo
	servidor.sendmail(remitente,email,mensaje.as_string())
	print("Correo enviado exitosamente a: {}".format(email))

# Nos desconectamos del servidor
servidor.quit()



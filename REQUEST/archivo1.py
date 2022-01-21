from importlib.metadata import requires
import requests
#get: metodo que nos ayhuda a extraer informacion

#get
peticion = requests.get('http://protecounam.mx/home', timeout=1) #Genera objeto de tipo response con la informacion del sitio
#timeout tiempo de espera de respuesta en segundos, es necesario ponerlo
#print(peticion.status_code) si recibe 200 es una pagina levantada
#print(help(peticion))
#print(peticion.content) #ver informacion del sitio en bytes sin formato
#print(peticion.text) #informacion con formato

#req_json = requests.get('https://api.github.com/',timeout=1)
req_json = requests.get('https://api.github.com/users/IvanMartinezIPN',timeout=1)
#print(req_json.json()) #ver informacion del archivo json
json_values = req_json.json()
print(type(json_values)) #regresa un diccionario
#print(json_values['current_user_url']) #imprimir valor del diccionario, es decir buscar valor por llaves
for items in json_values.items():
    #.items por diccionario
    print(items)
#HEADERS(ENCABEZADOS)
#PROPORCIONA INFORMACION DEL SITIO A TRAVES DE LOS ENCABEZADOS
req_headers = req_json.headers
#print(req_json.headers)
#print(type(req_headers))
#for items in req_headers.items():
#    print(items)

#POST nos permite obtener informacion al pasar datos por medio de formularios

#datos_dic = {'user':'Cesar', 'password': 'Hola123'}  #informacion a pasar a traves del formularo
#req_post = requests.post('https://httpbin.org/post',data=datos_dic)
#print(req_post.text)

#req_post_json = req_post.json()
#print(req_post_json['form']['password'])
#guardar una imagen

req_img = requests.get('http://protecounam.mx/img/base/principal_1.png')
#print(req_img.content)# informacion en bytes

#guardar elemento
file = open('imagen_muestra.png','wb') #escribir la imagen
file.write(req_img.content) #se guarda en la misma direccion del archivo
file.close()

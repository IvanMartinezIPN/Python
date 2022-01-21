from multiprocessing import connection
import sqlite3

def INITDatabase():
    conexion = sqlite3.connect('Cliente.db')
    conexion.commit()
    conexion.close()


def Crear_tabla_usuario():
    conexion = sqlite3.connect('Cliente.db')
    cur = conexion.cursor()
    cur.execute('CREATE TABLE usuario(id int, nombre varchar, edad int, estatura decimal, identificacion text);')
    conexion.commit()
    conexion.close()

def Agregar_usuario(lista):
    conexion = sqlite3.connect('Cliente.db')
    cur = conexion.cursor() #acciones con SQL
    cur.execute("INSERT INTO usuario (id, nombre,edad,estatura,identificacion) VALUES ({},'{}',{},{},'{}');".format(lista[0],lista[1],lista[2],lista[3],lista[4]))

    conexion.commit()
    conexion.close()

def Ver_registros():
    conexion = sqlite3.connect('Cliente.db')
    cur = conexion.cursor()
    cur.execute('SELECT * FROM usuario;')
    seleccion = cur.fetchall() #Pasa el objeto SQL para ser interpretado
    print('Registros :')
    for i in seleccion:
        print(i)

def Eliminar_usuario(id_usuario):
    conexion = sqlite3.connect('Cliente.db')
    cur = conexion.cursor()
    cur.execute('DELETE FROM usuario WHERE id = {};'.fomrat(id_usuario))
    print('Usuario eliminado')
    conexion.commit()
    conexion.close()

usuario1 = [316333879,'Martin Chilpa',22,1.80,'ide.pdf']

INITDatabase() 
#Crear_tabla_usuario()
#Agregar_usuario(usuario1)
Ver_registros()
Eliminar_usuario(316333879)
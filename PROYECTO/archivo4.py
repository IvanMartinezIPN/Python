import sqlite3
import sys
def Crear_usuario():
    conn = sqlite3.connect('BDusuarios.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE usuario (id_usuario int, nombre varchar, edad int, altura int, id text);')
    conn.commit()
    conn.close()


def Agregar_usuario(usuarios : list):
    conn = sqlite3.connect('BDusuarios.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO usuario (id_usuario, nombre, edad, altura, id) VALUES ({}, "{}", {}, {}, "{}");'.format(usuarios[0], usuarios[1],usuarios[2],usuarios[3],usuarios[4]))                                                                                                                                                                                                                     
    conn.commit()
    conn.close()

def Ver_usuarios():

    conn = sqlite3.connect('BDusuarios.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM usuario;')
    data = cur.fetchall()  
    return data


def Eliminar_usuario(usuario_id : int):
  
    conn = sqlite3.connect('BDusuarios.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM usuario WHERE id_usuario = {};'.format(usuario_id))
    conn.commit()
    conn.close()


def Actualizar_usuario(usuario_id : int, nombre : str, edad: int):
   
    conn = sqlite3.connect('BDusuarios.db')
    cur = conn.cursor()
    cur.execute('UPDATE usuario SET nombre = {}, edad = "{}" WHERE id_usuario  = {};'.format(nombre, edad, usuario_id))
    conn.commit()
    conn.close()


nuevos_usuarios = [
    [22,'Martin Chilpa',22,1.80,'ide.pdf'],
    [1,'Dante Olivares',23,1.95,'ide_D.pdf'],
    [2,'Edgar Ramirez',23,1.75,'id_E.pdf'],
    [3,'Daniel Garcia',24,1.70,'idD.pdf'],
]


if __name__ == "__main__":
    Crear_usuario()
    for nuevos in nuevos_usuarios:
        Agregar_usuario(nuevos)
    usuarios = Ver_usuarios()  
    print(usuarios)
    Eliminar_usuario(2)
    Eliminar_usuario(3)
    Actualizar_usuario(22, 24, 'Dante Armando')
    Actualizar_usuario(1, 33, 'Dante Flores') 
    cambios = Ver_usuarios()
    print(cambios)
    pass
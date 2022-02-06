import json # Para trabajar con archivos JSON

Asistente = [
    {
        'Nombre' : 'Dante Olivares',
        'Edad' : 23,
        'Correo' : 'dante.olivares@gmail.com',
        'Procedencia' : {
            'pnombre' : 'Externo',
            'Ubicacion' : 'Guadalajara'
        },
        'Cursos tomados' : {
            'Python Intermedio AM' : {
                'Turno': 'Matutino',
                'Estatus' : 'En curso' 
            }, 
            'Ciberseguridad' : {
                'Turno': 'Vespertino',
                'Estatus' : 'En curso'
            }, 
            'Redes de Computadoras' : {
                'Turno': 'Matutino',
                'Estatus' : 'En curso' 
            }
        },
        'Pago' : {
            'Estatus' : True,
            'Monto' : 1200.00,
            'Fecha' : '14/01/2022'
        }
    },
    {
        'Nombre' : 'Azul Olivares',
        'Edad' : 23,
        'Correo' : 'Azul.olivares@gmail.com',
        'Procedencia' : {
            'pnombre' : 'Externo',
            'Ubicacion' : 'Guadalajara'
        },
        'Cursos tomados' : {
            'Python Intermedio AM' : {
                'Turno': 'Matutino',
                'Estatus' : 'En curso' 
            }, 
            'Ciberseguridad' : {
                'Turno': 'Vespertino',
                'Estatus' : 'En curso'
            }, 
            'Redes de Computadoras' : {
                'Turno': 'Matutino',
                'Estatus' : 'En curso' 
            }
        },
        'Pago' : {
            'Estatus' : True,
            'Monto' : 1200.00,
            'Fecha' : '15/01/2022'
        }
    }
]
# Python a JSON
json_data = json.dumps(Asistente)

#JSON
with open('data.json', 'w') as json_file:
    json_file.write(json_data)
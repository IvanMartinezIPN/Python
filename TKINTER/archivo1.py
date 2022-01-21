from multiprocessing.sharedctypes import Value
from tkinter import * #Manda a llamar todos los archivos de Tkinter
from tkinter import ttk #Nuevos modulos de tkinter
#ROOT
main = Tk() #Creando un frame de tkinter
#CREANDO DISTINTOS frames

main_frame = ttk.Frame(main, padding='12 12').grid(column = 0,row = 0, sticky= E )
Button(main,text = 'Boton viejo').grid()

ttk.Button(main, text= 'Boton nuevo').grid()
#Labels
ttk.Label(main, text = 'Hola mundo').grid()
ttk.Label(main, text = 'Otro label').grid()

#Entry = input
ttk.Entry(main, width=50).grid()
#Radiobuttons
rb1 = ttk.Radiobutton(main, text = 'Alto', value = 'V1').grid()
rb2 = ttk.Radiobutton(main, text = 'Mediano', value = 'V2').grid()
rb3 = ttk.Radiobutton(main, text = 'Chico', value = 'V3').grid()

#Frame, nos ayuda a contener widgets 


main.mainloop()
#print('Mensaje despues de cerrar terminal')
#Lo debajo de mainloop no se va a ejecutar hasta que cierre la ventana de la aplicacion
#El codigo debajo no se va a ejecutar hasta que cierre la ventana de aplicacion



import tkinter as tk
from tkinter import ttk

global nombre, edad, genero
def nueva_ventana():
    nueva_ventana = tk.Toplevel(nuevo)
    nueva_ventana.geometry('150x150')
    nueva_ventana.title("Datos")
    ttk.Label(nueva_ventana, text="Nombre: ").grid(sticky=tk.S)
    ttk.Label(nueva_ventana, text=nombre.get()).grid(sticky=tk.S)
    ttk.Label(nueva_ventana, text="Edad: ").grid(sticky=tk.S)
    ttk.Label(nueva_ventana, text=edad.get()).grid(sticky=tk.S)
    ttk.Label(nueva_ventana, text="Genero: ").grid(sticky=tk.S)
    ttk.Label(nueva_ventana, text=genero.get()).grid(sticky=tk.S)
nuevo = tk.Tk()
nuevo.title('Datos')
main_frame = ttk.Frame(nuevo, padding='12 12').grid(column = 0,row = 0)
nombre = tk.StringVar()
edad = tk.IntVar()
genero = tk.StringVar()

ttk.Label(main_frame,width=50, text="Ingresa tu nombre: ").grid(sticky=tk.S)
ttk.Entry(main_frame,width=30, textvariable=nombre).grid()
ttk.Label(main_frame,width=50,text="Ingresa tu edad: ").grid(sticky=tk.S)
ttk.Entry(main_frame, textvariable= edad).grid()
ttk.Label(main_frame, text="Ingresa tu genero: ").grid()
ttk.Radiobutton(main_frame, text="Masculino", value="Masculino", variable=genero,).grid(sticky=tk.S)
ttk.Radiobutton(main_frame, text="Femenino", value="Femenino", variable=genero).grid(sticky=tk.S)
ttk.Radiobutton(main_frame, text="Otro", value="Otro", variable=genero).grid(sticky=tk.S)
ttk.Button(main_frame, text="Registrar", command=nueva_ventana).grid()

tk.mainloop()
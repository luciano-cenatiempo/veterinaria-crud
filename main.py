from tkinter import *
from clientes import *
from mascotas import *
from database import *
from agregar_mascotas import abrir_agregar_mascotas
from agregar_clientes import abrir_nuevo_cliente
from estilos import * 

# Defino la ventana principal de mi programa
root = Tk()
root.geometry("500x700")
marco_principal = Frame(root)
menubar=Menu(root)


menubasedat=Menu(menubar, tearoff=0)
menubasedat.add_command(label="Crear BBDD", command= crear_base_datos)
menubasedat.add_command(label="Salir", command= lambda: root.destroy())
menubar.add_cascade(label="BBDD", menu = menubasedat)
root.config(menu = menubar, bg= "lightblue")
# Label titulo
menu_titulo = Label(root, text= "Veterinaria", bg= "lightblue", font=("Comic Sans Ms", 35 , "bold"))
menu_titulo.pack(pady= 3)

# marco botones
marco = Frame(root, bg= "lightblue")
marco.pack( pady= 15)



# botones 

btn_clientes = Button(marco, text="Visualizar Clientes", bg= color_boton, width = 25, fg= texto_blanco, font=("Arial", 18 , "bold"), command= abrir_clientes )
btn_clientes.pack(pady= 2)

btn_mascotas = Button(marco, text="Visualizar Mascotas", bg= color_boton, width = 25, fg= texto_blanco, font=("Arial", 18 , "bold"), command= abrir_mascotas)
btn_mascotas.pack(pady= 2)

btn_agregar_cliente = Button(marco, text="Agregar clientes", bg= color_boton, width = 25, fg= texto_blanco, font=("Arial", 18 , "bold"), command= abrir_nuevo_cliente )
btn_agregar_cliente.pack(pady= 2)

btn_agregar_mascotas = Button(marco, text="Agregar mascotas", bg= color_boton, width = 25, fg= texto_blanco, font=("Arial", 18 , "bold"), command= abrir_agregar_mascotas )
btn_agregar_mascotas.pack(pady= 2)

root.mainloop()
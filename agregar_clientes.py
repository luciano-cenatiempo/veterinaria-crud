from tkinter import *

from funciones import *
from estilos import *

# -------------------------- Ventana Nuevo Cliente -----------------------------------------------
def abrir_nuevo_cliente():

    # Variables de ingreso
    input_nombre = StringVar()
    input_apellido = StringVar()
    input_dni = StringVar()
    input_telefono = StringVar()
   
    
    w_nuevo_cliente = Toplevel()
    w_nuevo_cliente.title("Nuevo cliente")
    w_nuevo_cliente.geometry("700x400")
    w_nuevo_cliente.config(bg = "lightblue")
    lbl_titulo = Label(w_nuevo_cliente, text= "Añadir Clientes", bg= "lightblue", font=("Arial", 25 , "bold"))
    lbl_titulo.pack()
    frm_cliente = LabelFrame(w_nuevo_cliente, text= "Añadir nuevo cliente", padx= 3, pady= 3, font=("Arial", 14 ))
    frm_cliente.config(width= 500)
    lbl_nombre = Label(frm_cliente, text= "Nombre:", font=("Arial", 14 , "bold"))
    lbl_nombre.grid(row= 0 , column= 1, padx = 3 , pady= 3)
    txt_nombre = Entry( frm_cliente, font=("Arial", 14 ), textvariable=input_nombre )
    txt_nombre.grid(row= 0 , column= 2, padx = 3 , pady= 3)
    lbl_apellido = Label(frm_cliente, text= "Apellido:", font=("Arial", 14 , "bold"))
    lbl_apellido.grid(row= 1 , column= 1, padx = 3 , pady= 3)
    txt_apellido = Entry( frm_cliente , font=("Arial", 14 ), textvariable=input_apellido)
    txt_apellido.grid(row= 1 , column= 2, padx = 3 , pady= 3)
    lbl_dni = Label(frm_cliente, text= "Dni:", font=("Arial", 14 , "bold"))
    lbl_dni.grid(row= 2 , column= 1, padx = 3 , pady= 3)
    txt_dni = Entry( frm_cliente, font=("Arial", 14 ), textvariable=input_dni)
    txt_dni.grid(row= 2, column= 2, padx = 3 , pady= 3)
    lbl_telefono = Label(frm_cliente, text= "Telefono:", font=("Arial", 14 , "bold"))
    lbl_telefono.grid(row= 3 , column= 1, padx = 3 , pady= 3)
    txt_telefono = Entry( frm_cliente, font=("Arial", 14 ), textvariable=input_telefono)
    txt_telefono.grid(row= 3, column= 2, padx = 3 , pady= 3)
    btn_agregaruno = Button(frm_cliente,font=("Arial", 12 ),fg=texto_blanco, bg = color_boton, text="Añadir", command = lambda: agregar_cliente(input_nombre.get(),input_apellido.get(), input_dni.get(), input_telefono.get(), w_nuevo_cliente))
    btn_agregaruno.grid(row= 4, column= 3, padx = 3 , pady= 3)
    
    frm_cliente.pack()
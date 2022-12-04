from tkinter import *
from tkinter import ttk

from estilos import *

import database as db
from funciones import *
from form_mascotas import form_agregar_mascotas

def mostrar_info_duenio(id, nombre_duenio , apellido_duenio): # Muestra la información del dueño que se selecciona en combobox
    datos_duenio = db.select_duenio(id)
    nombre_duenio.set(datos_duenio[0])
    apellido_duenio.set(datos_duenio[1])


# --------------------VENTANA DE AGREGAR MASCOTA--------------
def abrir_agregar_mascotas():

    # Variables de ingreso
    input_id_duenio = StringVar()
    nombre_duenio = StringVar()
    apellido_duenio = StringVar()

    try: 
        combo_duenios = db.armar_combo_duenios() # Arma el combobox con id_cliente
        
    except:
        combo_duenios = []
        messagebox.showerror("Error", "Debe crear la base de datos antes de continuar")
        return

    # Defino la ventana
    w_agregar_mascotas = Toplevel()
    w_agregar_mascotas.title("Agregar Mascota")
    w_agregar_mascotas.geometry("700x400")
    w_agregar_mascotas.config(bg = "lightblue")
    

    # Frame para elegir dueño
    lbl_titulo = Label(w_agregar_mascotas, text= "Añadir Mascotas", bg= "lightblue", font=("Arial", 25 , "bold"))
    lbl_titulo.pack()
    frm_duenio = LabelFrame(w_agregar_mascotas, text= "Elegir dueño", padx= 3, pady= 3, font=("Arial", 14 ))
    frm_duenio.config(width= 500)
    
    # Combobox para elegir ID
    lbl_id_duenio = Label(frm_duenio, text= "Id del dueño:", font=("Arial", 14 , "bold"))
    lbl_id_duenio.grid(row= 0 , column= 1, padx = 3 , pady= 3)
    cmb_id_duenio = ttk.Combobox( frm_duenio, textvariable= input_id_duenio,values=combo_duenios, font=("Arial", 14), state="readonly")
    cmb_id_duenio.grid(row= 0 , column= 2, padx = 3 , pady= 3)
    cmb_id_duenio.bind("<<ComboboxSelected>>", lambda _ : mostrar_info_duenio(cmb_id_duenio.get(),nombre_duenio,apellido_duenio))
    
    # Datos del dueño
    lbl_nombre_duenio = Label( frm_duenio, font=("Arial", 14 ), textvariable= nombre_duenio )
    lbl_nombre_duenio.grid(row= 1 , column= 1, padx = 3 , pady= 3)
    
    lbl_apellido_duenio = Label( frm_duenio , font=("Arial", 14 ), textvariable= apellido_duenio)
    lbl_apellido_duenio.grid(row= 1 , column= 2, padx = 3 , pady= 3)
    
    # Boton para elegir dueño (abre el formulario para agregar mascotas)
    btn_elegir_duenio = Button(frm_duenio,font=("Arial", 12 ), bg = color_boton, fg=texto_blanco , text="Añadir mascota a este dueño", command = lambda: form_agregar_mascotas('Agregar', cmb_id_duenio.get(),w_agregar_mascotas))
    btn_elegir_duenio.grid(row= 4, column= 3, padx = 3 , pady= 3)
    
    frm_duenio.pack()
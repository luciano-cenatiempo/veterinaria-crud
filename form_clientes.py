from tkinter import *
from tkinter import messagebox

import database as db
from estilos import *
def form_editar_clientes(id):

    # Variables de ingreso
    input_nombre = StringVar()
    input_apellido = StringVar()
    input_dni = StringVar()
    input_telefono = StringVar()
    
    # Dependiendo del modo la variable id equivale al id de mascota o al id del dueño
    
    datos_cliente = db.buscar_cliente(id)
    if not datos_cliente:
        messagebox.showinfo("Atención", "Este cliente ya no existe, porfavor actualizar lista con 'mostrar todos'")
        return
    
    # Asigno los valores de la base de datos    
    input_nombre.set(datos_cliente[0])
    input_apellido.set(datos_cliente[1])
    input_dni.set(datos_cliente[2])
    input_telefono.set(datos_cliente[3])
    
    # Defino la ventana
    w_form_clientes = Toplevel()
    w_form_clientes.title( "Editar cliente")
    w_form_clientes.geometry("700x700")
    w_form_clientes.config(bg = "lightblue")
    
    
    lbl_titulo = Label(w_form_clientes, text= "Editar cliente", bg= "lightblue", font=("Comic Sans Ms", 35 , "bold"))
    lbl_titulo.pack( pady= 3)
    frm_formulario = Frame(w_form_clientes, padx= 3, pady= 3)
    frm_formulario.config(width= 500)
    
    

    
    lbl_id = Label(frm_formulario, text= f"Id del cliente: {id}", font=("Arial", 14 , "bold"))
    lbl_id.pack(pady=3) 
    lbl_nombre = Label(frm_formulario, text= "Nombre", font=("Arial", 14 , "bold"))
    lbl_nombre.pack(pady=3)
    txt_nombre = Entry(frm_formulario, textvariable= input_nombre, font=("Arial", 14 ))
    txt_nombre.pack( pady=3, padx= 5)

    lbl_apellido = Label(frm_formulario, text= "Apellido", font=("Arial", 14 , "bold"))
    lbl_apellido.pack(pady= 3)
    txt_apellido = Entry(frm_formulario, textvariable= input_apellido, font=("Arial", 14 ))
    txt_apellido.pack(pady=3, padx= 5)

    lbl_dni = Label(frm_formulario, text= "Dni", font=("Arial", 14 , "bold"))
    lbl_dni.pack(pady=3)
    txt_dni = Entry(frm_formulario, textvariable= input_dni, font=("Arial", 14 ))
    txt_dni.pack(pady=3, padx= 5)

    lbl_telefono = Label(frm_formulario, text= "Telefono", font=("Arial", 14 , "bold"))
    lbl_telefono.pack(pady=3)
    txt_telefono = Entry(frm_formulario, textvariable= input_telefono, font=("Arial", 14 ))
    txt_telefono.pack(pady=3, padx= 5)
    
    
    
    btn_editar = Button(frm_formulario,font=("Arial", 12 ),fg=texto_blanco, bg = color_boton, text= "Editar", command = lambda: db.editar_cliente(id,input_nombre.get(), input_apellido.get(), input_dni.get(), input_telefono.get(), w_form_clientes))
    btn_editar.pack(pady= 5)

    btn_eliminar = Button(frm_formulario,font=("Arial", 12 ),fg=texto_blanco, bg = "red", text= "Eliminar", command = lambda: db.eliminar_cliente(id, w_form_clientes))
    btn_eliminar.pack(pady= 5)
    
    frm_formulario.pack(pady= 15, padx= 15)
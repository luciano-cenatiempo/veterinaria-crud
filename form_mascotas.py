from tkinter import *
from tkinter import ttk

import database as db
from funciones import *
from estilos import *
def form_agregar_mascotas(modo,id, ventana):
    if modo == "Agregar" and id == "":
        messagebox.showinfo("Atención", "Debe seleccionar un dueño primero",parent = ventana)
        return
    # Variables de ingreso
    input_nombre_mascota = StringVar()
    input_animal = StringVar()
    input_edad = StringVar()

    # Dependiendo del modo la variable id equivale al id de mascota o al id del dueño
    if modo == "Editar":
        id_mascota = id
        datos_mascota = db.buscar_mascota(id_mascota) # lleno el formulario con los datos actuales
        
        if not datos_mascota:
            messagebox.showinfo("Atencion", "Esta mascota ya no existe, actualice con el botón 'Mostrar todos'")
            return
        
        input_nombre_mascota.set(datos_mascota[0])
        input_animal.set(datos_mascota[1])
        input_edad.set(datos_mascota[2])
    
    elif modo == "Agregar":
        id_duenio = id
    #combo_duenios = db.armar_combo_duenios() # Trae de la BBDD los ids de los clientes existentes

    # Defino la ventana
    w_form_mascotas = Toplevel()
    w_form_mascotas.title(f"{modo} mascota")
    w_form_mascotas.geometry("700x700")
    w_form_mascotas.config(bg = "lightblue")
    
    # Frame para elegir dueño
    lbl_titulo = Label(w_form_mascotas, text= f"{modo} Mascota", bg= "lightblue", font=("Comic Sans Ms", 35 , "bold"))
    lbl_titulo.pack( pady= 3)
    frm_formulario = Frame(w_form_mascotas, padx= 3, pady= 3)
    frm_formulario.config(width= 500)
    
    # Se muestra el id de la mascota que se está editando o el id del dueño al que se le está agregando la mascota

    if modo == "Editar":
        lbl_id = Label(frm_formulario, text= f"Id de la mascota: {id_mascota}", font=("Arial", 14 , "bold"))
        lbl_id.pack(pady=3) 
    elif modo == "Agregar":
        lbl_id = Label(frm_formulario, text= f"Id del dueño: {id_duenio}", font=("Arial", 14 , "bold"))
        lbl_id.pack(pady=3) 
    lbl_nombre = Label(frm_formulario, text= "Nombre", font=("Arial", 14 , "bold"))
    lbl_nombre.pack(pady=3)
    txt_nombre = Entry(frm_formulario, textvariable= input_nombre_mascota, font=("Arial", 14 ))
    txt_nombre.pack( pady=3, padx= 5)

    lbl_animal = Label(frm_formulario, text= "Animal", font=("Arial", 14 , "bold"))
    lbl_animal.pack(pady= 3)
    txt_animal = Entry(frm_formulario, textvariable= input_animal, font=("Arial", 14 ))
    txt_animal.pack(pady=3, padx= 5)

    lbl_edad = Label(frm_formulario, text= "Edad:", font=("Arial", 14 , "bold"))
    lbl_edad.pack(pady=3)
    txt_edad = Entry(frm_formulario, textvariable= input_edad, font=("Arial", 14 ))
    txt_edad.pack(pady=3, padx= 5)
    # Datos del dueño
    
    if modo == "Agregar":
        btn_agregar = Button(frm_formulario,font=("Arial", 12 ), fg=texto_blanco, bg = color_boton, text= modo, command = lambda: db.agregar_o_editar_animal("Agregar",input_nombre_mascota.get(), input_animal.get(),input_edad.get(), id_duenio, w_form_mascotas))
        btn_agregar.pack(pady= 5)
    elif modo == "Editar":
        btn_editar = Button(frm_formulario,font=("Arial", 12 ),fg=texto_blanco, bg = color_boton, text= modo, command = lambda: db.agregar_o_editar_animal("Editar",input_nombre_mascota.get(), input_animal.get(),input_edad.get(), id_mascota, w_form_mascotas))
        btn_editar.pack(pady= 5)
        btn_eliminar = Button(frm_formulario,font=("Arial", 12 ),fg=texto_blanco, bg = "red", text= "Eliminar", command = lambda: db.eliminar_mascota(id, w_form_mascotas))
        btn_eliminar.pack(pady= 5)
    
    frm_formulario.pack(pady= 15, padx= 15)
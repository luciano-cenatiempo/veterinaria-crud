from tkinter import *
from tkinter import ttk

from funciones import *
from estilos import *

# Ventana de visualizar mascotas
def abrir_mascotas (): 
    try: 
        combo_duenios = db.armar_combo_duenios() # Arma el combobox con id_cliente
        combo_duenios.append('') # Le agrego el valor de seleccion vacio
    except: # Si no hay conexion con la BBDD
        combo_duenios = []
        messagebox.showerror("Error", "Debe crear la base de datos antes de continuar")
        return 
    w_visualizar_mascotas = Toplevel()
    w_visualizar_mascotas.title("Mascotas")
    w_visualizar_mascotas.config(bg = "lightblue")

    input_id_duenio = StringVar()
    input_nombre_mascota = StringVar()

    # --------- Buscador de clientes --------


    mascotas_titulo = Label(w_visualizar_mascotas, text= "Mascotas", bg= "lightblue", font=("Comic Sans Ms", 35 , "bold"))
    mascotas_titulo.pack(pady = 3)

    mascotas_buscador = LabelFrame(w_visualizar_mascotas, text= "Buscar mascotas", padx= 3, pady= 3, font=("Arial", 14 ))
    mascotas_buscador.config(width=400)
    mascotas_buscador.pack(pady= 5, padx=15)

    lbl_id = Label(mascotas_buscador, text= "ID cliente:", font=("Arial", 14 , "bold"))
    lbl_id.grid(row= 0 , column= 1, padx = 3 , pady= 3)
    cmb_id = ttk.Combobox( mascotas_buscador, textvariable= input_id_duenio,values=combo_duenios, font=("Arial", 14), state = "readonly")
    cmb_id.grid(row= 0 , column= 2, padx = 3 , pady= 3)
    lbl_nombre = Label(mascotas_buscador, text= "Nombre mascota:", font=("Arial", 14 , "bold"))
    lbl_nombre.grid(row= 0 , column= 3, padx = 3 , pady= 3)
    txt_nombre = Entry( mascotas_buscador, textvariable=input_nombre_mascota, font=("Arial", 14) )
    txt_nombre.grid(row= 0, column= 4, padx = 3 , pady= 3)
    btn_buscar = Button(mascotas_buscador, text="Buscar", fg=texto_blanco, bg = color_boton, font=("Arial", 14 ), command= lambda:buscar_mascotas(input_id_duenio.get(), input_nombre_mascota.get(), tabla, w_visualizar_mascotas))
    btn_buscar.grid(row= 1 , column= 2, padx = 3 , pady= 3)
    btn_listar = Button(mascotas_buscador, text="Mostrar todos", fg=texto_blanco, bg = color_boton, font=("Arial", 14 ), command= lambda: mostrar_todas_mascotas(tabla))
    btn_listar.grid(row= 1 , column= 3, padx = 3 , pady= 3)

    #------------------- Listado de mascotas -------------------

    mascotas_listado = LabelFrame(w_visualizar_mascotas, text= "Lista Mascotas", padx= 3, pady= 3, font=("Arial", 14 ))
    mascotas_listado.config(width=800)
    mascotas_listado.pack(pady=5, padx=15)
    
    tabla = armar_tabla(["Nombre Mascota","Animal", "Edad", "Id dueño","Apellido Dueño","Nombre dueño"], mascotas_listado)

    tabla.pack()

    # Se traen todos los clientes de la base de datos y se muestran
    mostrar_todas_mascotas(tabla)

from tkinter import *

from funciones import *
from estilos import *


def abrir_clientes (): 
    w_visualizar_clientes = Toplevel()
    w_visualizar_clientes.title("Clientes")
    w_visualizar_clientes.geometry("700x700")
    w_visualizar_clientes.config(bg = "lightblue")

    # Variables de input
    input_apellido = StringVar()
    input_dni = StringVar()

    # --------- Buscador de clientes --------

    clientes_titulo = Label(w_visualizar_clientes, text= "Visualizar Clientes", bg= "lightblue", font=("Comic Sans Ms", 35 , "bold"))
    clientes_titulo.pack(pady=3)

    clientes_buscador = LabelFrame(w_visualizar_clientes, text= "Buscar clientes", padx= 3, pady= 3, font=("Arial", 14 ))
    clientes_buscador.config(width=400)
    clientes_buscador.pack(pady= 5, padx= 15)

    lbl_apellido = Label(clientes_buscador, text= "Apellido:", font=("Arial", 14 , "bold"))
    lbl_apellido.grid(row= 0 , column= 1, padx = 3 , pady= 3)
    txt_apellido = Entry( clientes_buscador, textvariable= input_apellido, font=("Arial", 14))
    txt_apellido.grid(row= 0 , column= 2, padx = 3 , pady= 3)
    lbl_dni = Label(clientes_buscador, text= "DNI:", font=("Arial", 14 , "bold"))
    lbl_dni.grid(row= 0 , column= 3, padx = 3 , pady= 3)
    txt_dni = Entry( clientes_buscador, textvariable=input_dni, font=("Arial", 14) )
    txt_dni.grid(row= 0, column= 4, padx = 3 , pady= 3)
    btn_buscar = Button(clientes_buscador, text="Buscar",fg=texto_blanco, bg = color_boton, font=("Arial", 14 ), command= lambda:buscar_clientes(input_apellido.get(), input_dni.get(), tabla, w_visualizar_clientes))
    btn_buscar.grid(row= 1 , column= 2, padx = 3 , pady= 3)
    btn_listar = Button(clientes_buscador, text="Mostrar todos", fg=texto_blanco, bg = color_boton, font=("Arial", 14 ), command= lambda: mostrar_todos_resultados(tabla))
    btn_listar.grid(row= 1 , column= 3, padx = 3 , pady= 3)

    #------------------- Listado de clientes -------------------

    clientes_listado = LabelFrame(w_visualizar_clientes, text= "Lista clientes", padx= 3, pady= 3, font=("Arial", 14 ))
    clientes_listado.config(width=800)
    clientes_listado.pack(pady= 5, padx= 15)
    
    tabla = armar_tabla(["Nombre","Apellido", "Dni", "Telefono"], clientes_listado)

    tabla.pack()

    # Se traen todos los clientes de la base de datos y se muestran
    mostrar_todos_resultados(tabla)






    



from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from form_mascotas import form_agregar_mascotas
from form_clientes import form_editar_clientes
import database as db


def armar_tabla(lista_campos, lugar): # Genera la tabla en pantalla ( columnas sin valores)
    columnas = []
    # armo las columnas para la tabla, tiene que ser una menos porque la #0 ya está definida
    for n in range (0, len(lista_campos)):
        columnas.append(f"#{n+1}")

    
    tabla = ttk.Treeview(lugar, columns = columnas)

    # La columna #0 es la que viene definida y la usamos para el id
    tabla.column("#0",width=80, anchor= CENTER)
    tabla.heading("#0", text="Id")
    
    # Agregamos nuestras columnas
    n = 0
    for columna in columnas:
        
        tabla.column(columna, anchor = CENTER)
        tabla.heading(columna, text = lista_campos[n])
        n += 1
    
    return tabla



def cargar_tabla(lista, tabla, entidad): # Carga las tablas con los valores
    if len(lista)>0:
        for elemento in lista:
            tabla.insert( "", "end",text=elemento[0], values=elemento[1:])
            tabla.bind("<Double-1>", lambda evento: on_doble_click(evento, tabla, entidad))

def on_doble_click(evento, tabla, entidad): # Toma el id del registro y abre el formulario para actualizar o eliminar
    item_id = tabla.selection()[0]
    item_id_text = tabla.item(item_id)["text"]
    
    # Si la tabla es una tabla de mascotas entonces llama a un formulario distinto al de clientes
    if entidad == 'mascotas':
        form_agregar_mascotas("Editar",item_id_text, None)
    elif entidad == 'clientes':
        form_editar_clientes(item_id_text)
        

# Funcion para validar los datos ingresados en el cliente
def validar_cliente(nombre, apellido, dni, telefono, ventana):
    try:
        dni = int(dni)
        telefono = int(telefono)
    except:
        messagebox.showwarning("Error","El DNI ingresado o el Telefono tienen un formato invalido", parent = ventana)
        return False
    if len(nombre) > 30 or nombre == "":
        messagebox.showwarning("Error", "El campo nombre no puede estar vacío y debe tener menos de 30 caracteres", parent = ventana)
        return False
    elif apellido == "" or len(apellido)>30:
        messagebox.showwarning("Error", "El campo apellido no puede estar vacío y debe tener menos de 30 caracteres", parent = ventana)
        return False
    elif dni > 99_999_999  or dni <= 0:
        messagebox.showwarning("Error", "Valores invalidos para DNI", parent = ventana)
        print(dni)
        return False
    elif telefono > 999_999_999_999 or telefono < 0: 
        messagebox.showwarning("Error", "Valores invalidos para telefono", parent = ventana)
        return False
    else:
        return True

def borrar_tabla(tabla): # Borra las tablas de la pantalla
    tabla.delete(*tabla.get_children())

# -------------------- Clientes  ----------------   
def agregar_cliente(nombre, apellido, dni, telefono, ventana): 
    # Quito los espacios en blanco
    nombre = nombre.strip()
    apellido = apellido.strip()
    dni = dni.strip()
    telefono = telefono.strip()
    
    # Valida los datos para agregarlos
    if validar_cliente(nombre, apellido, dni, telefono, ventana):
        db.agregar_cliente(nombre, apellido, dni, telefono, ventana)
            

def mostrar_todos_resultados(tabla): # Muestra todos los clientes en pantalla
    lista = db.mostrar_clientes_todos() 
    borrar_tabla(tabla)
    cargar_tabla(lista,tabla,"clientes")

def buscar_clientes(apellido, dni, tabla, ventana): # Muestra los clientes en pantalla segun los filtros de busqueda
    lista = db.filtrar_clientes(apellido, dni, ventana)
    borrar_tabla(tabla)
    cargar_tabla(lista, tabla, "clientes")




# ---------------- Mascotas----------------------

def mostrar_todas_mascotas(tabla): # muestra en pantalla todas las mascotas
    lista = db.mostrar_mascotas_todas() 
    borrar_tabla(tabla)
    cargar_tabla(lista, tabla, "mascotas")

def buscar_mascotas(id_duenio, nombre_mascota, tabla, ventana): # Muestra en pantalla solo las mascotas que coincidan con el filtro
    lista = db.filtrar_mascotas(id_duenio, nombre_mascota, ventana)
    borrar_tabla(tabla)
    cargar_tabla(lista, tabla, "mascotas")

def validar_mascota(nombre, animal , edad, ventana):
    try:
        edad = int(edad)
    except:
        messagebox.showwarning("Error","La edad ingresada tiene un formato invalido", parent = ventana)
        return False
    if len(nombre) > 20 or nombre == "":
        messagebox.showwarning("Error", "El campo nombre no puede estar vacío o tener más de 20 caracteres", parent = ventana)
        return False
    elif animal == "" or len(animal) > 20:
        messagebox.showwarning("Error", "El campo Animal no puede estar vacío o tener más de 20 caracteres", parent = ventana)
        return False
    elif edad <=0:
        messagebox.showwarning("Error", "Valores invalidos para edad", parent = ventana)
        return False
    else:
        return True




    

    
import sqlite3 as sql
from tkinter import messagebox
import funciones as fn


def crear_tabla_clientes():
    conexion = sql.connect("veterinariaDB")
    cursor = conexion.cursor()
    cursor.execute('''
            CREATE TABLE clientes (
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(30),
            apellido VARCHAR(30),
            dni int(8),
            telefono int(12))
    ''')
    conexion.commit()
    conexion.close()
    
    

def crear_tabla_mascotas():
    conexion = sql.connect("veterinariaDB")
    cursor = conexion.cursor()
    cursor.execute('''
            CREATE TABLE mascotas (
            id_mascota INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(20),
            animal VARCHAR(20),
            edad int(2),
            id_cliente int,
            foreign key (id_cliente) REFERENCES clientes(id_cliente))
        ''')
    conexion.commit()
    conexion.close()

def crear_base_datos():
    try:
        conexion = sql.connect("veterinariaDB")
        conexion.commit()
        crear_tabla_clientes()
        crear_tabla_mascotas()
        messagebox.showinfo("BBDD", "La base de datos fue creada con exito")
        conexion.close()

    except:
        messagebox.showwarning("BBDD", "La base de datos ya existe, no fue necesario volverla a crear")
        conexion.close()


def agregar_cliente(nombre, apellido, dni, telefono, ventana):
    
    try:
        conexion = sql.connect("veterinariaDB")
        cursor = conexion.cursor()
        datos = nombre, apellido, dni, telefono
        cursor.execute('INSERT INTO clientes values(NULL,?,?,?,?)', (datos))
        conexion.commit()
        messagebox.showinfo("Agregar cliente", "Cliente agregado correctamente" , parent = ventana)
        conexion.close()
        ventana.destroy()
    except:
        messagebox.showerror("Error", "Hubo un error al intentar añadir registro, comuniquese con el administrador", parent = ventana)
        conexion.close()


def mostrar_clientes_todos():
    try:
        conexion = sql.connect("veterinariaDB")
        cursor = conexion.cursor()
        cursor.execute('SELECT * from clientes')
        resultados = cursor.fetchall()
        conexion.close()
        return resultados
    except: 
         messagebox.showerror("Error", "Hubo un error al intentar mostrar los registros, comuniquese con el administrador")
         conexion.close()
         return []
    
def filtrar_clientes( apellido, dni, ventana):
    try:
        conexion = sql.connect("veterinariaDB")
        cursor = conexion.cursor()
        
        if  apellido != "" and dni !="":
            cursor.execute(f"SELECT * FROM clientes WHERE  apellido LIKE '%{apellido}%' AND dni LIKE '%{dni}%'")
            resultados = cursor.fetchall()
        elif apellido !="" and dni =="":
            cursor.execute(f"SELECT * FROM clientes WHERE apellido LIKE '%{apellido}%'")
            resultados = cursor.fetchall() 
        elif dni !="" and apellido == "":
            cursor.execute(f"SELECT * FROM clientes WHERE dni LIKE '%{dni}%'")
            resultados = cursor.fetchall()
        else:
            messagebox.showwarning("Atencion!", "No ingresó ningun parametro para busqueda" , parent = ventana)
            resultados = []
        conexion.close()
        return resultados

    except:
        messagebox.showwarning("Atencion!", "No hay resultados para la busqueda, intente con otra", parent = ventana)
        conexion.close()
        return []
        
def buscar_cliente(id):
    try:
        conexion = sql.connect("veterinariaDB")
        cursor = conexion.cursor()
        cursor.execute(f"SELECT nombre, apellido, dni, telefono FROM clientes where id_cliente = {id} ")
        resultados = cursor.fetchone()
        conexion.close()
        return resultados

    except: 
        messagebox.showerror("Error", "Hubo un error a la hora de obtener los datos del cliente")
        conexion.close()

def actualizar_cliente(id, nombre, apellido, dni, telefono, ventana):
    try :
        conexion = sql.connect("veterinariaDB")
        cursor = conexion.cursor()
        dni = int(dni)
        telefono = int(telefono)
        
        cursor.execute(f"UPDATE clientes SET nombre = '{nombre}', apellido = '{apellido}', dni = {dni}, telefono = '{telefono}' WHERE id_cliente = {id}")
        conexion.commit()
        
        messagebox.showinfo("Editar", "Cliente editado con éxito", parent = ventana)
        conexion.close()
        ventana.destroy()
        return True
    except :
        messagebox.showerror("Error", "No fue posible editar el cliente", parent = ventana)
        conexion.close()
        return False

def editar_cliente(id, nombre, apellido, dni, telefono , ventana):
    
    nombre = nombre.strip()
    apellido = apellido.strip()
    dni = dni.strip()
    telefono = telefono.strip()

    if not fn.validar_cliente(nombre, apellido, dni , telefono, ventana):
        return
    actualizo = actualizar_cliente(id, nombre, apellido, dni, telefono, ventana)
    if actualizo:
        ventana.destroy()

def eliminar_cliente(id,ventana): 
    try:
        conexion = sql.connect("veterinariaDB")
        cursor = conexion.cursor()
        cursor.execute(f"DELETE FROM clientes WHERE id_cliente = {id}")
        conexion.commit()
        messagebox.showinfo("Eliminar cliente", "Cliente eliminado con exito", parent = ventana)
        conexion.close()
        ventana.destroy()

    except: 
        messagebox.showerror("Error", "No se pudo eliminar el cliente", parent = ventana)
        conexion.close()
         


# --------------------- Mascotas --------------------------------

def mostrar_mascotas_todas(): # Muestra todas las mascotas en pantalla
    try:
        conexion = sql.connect("veterinariaDB")
        cursor = conexion.cursor()
        cursor.execute('SELECT a.id_mascota, a.nombre , a.animal, a.edad, a.id_cliente, b.apellido, b.nombre FROM mascotas as a LEFT JOIN clientes as b ON a.id_cliente = b.id_cliente')
        resultados = cursor.fetchall()
        conexion.close()
        return resultados
    except: 
         messagebox.showerror("Error", "Hubo un error al intentar mostrar los registros, comuniquese con el administrador")
         conexion.close()
         return []


def filtrar_mascotas(id_duenio, nom_mascota, ventana): # Busca mascotas usando el filtro
    try:
        conexion = sql.connect("veterinariaDB")
        cursor = conexion.cursor()
        
        resultados = []
        if  id_duenio != "" and nom_mascota !="" :
            cursor.execute(f"SELECT a.id_mascota, a.nombre , a.animal, a.edad, a.id_cliente, b.apellido, b.nombre FROM mascotas as a LEFT JOIN clientes as b ON a.id_cliente = b.id_cliente WHERE a.id_cliente = {id_duenio} AND a.nombre LIKE '%{nom_mascota}%'")
            resultados = cursor.fetchall()
            
        elif id_duenio != "" and nom_mascota == "":
            cursor.execute(f"SELECT a.id_mascota, a.nombre , a.animal, a.edad, a.id_cliente, b.apellido, b.nombre FROM mascotas as a LEFT JOIN clientes as b ON a.id_cliente = b.id_cliente WHERE a.id_cliente = {id_duenio}")
            resultados = cursor.fetchall()
            
        elif id_duenio == "" and nom_mascota != "":
            cursor.execute(f"SELECT a.id_mascota, a.nombre , a.animal, a.edad, a.id_cliente, b.apellido, b.nombre FROM mascotas as a LEFT JOIN clientes as b ON a.id_cliente = b.id_cliente WHERE a.nombre LIKE '%{nom_mascota}%'")
            resultados = cursor.fetchall()
            
        else:
            messagebox.showwarning("Atencion!", "No ingresó ningun parametro para busqueda", parent = ventana)
        conexion.close()    
        return resultados

    except:
        messagebox.showwarning("Atencion!", "Hubo un error al realizar la busqueda", parent = ventana)
        return []





def armar_combo_duenios(): # Arma el combobox con ids de dueños
    conexion = sql.connect("veterinariaDB")
    cursor = conexion.cursor()
    cursor.execute(f"SELECT id_cliente FROM clientes")
    resultados = cursor.fetchall()
    conexion.close()
    return resultados


def select_duenio(id): # Busca el nombre y apellido del dueño al seleccionar un id en el combobox
    conexion = sql.connect("veterinariaDB")
    cursor = conexion.cursor()
    cursor.execute(f"SELECT nombre, apellido FROM clientes where id_cliente = {id} ")
    resultados = cursor.fetchone()
    conexion.close()
    return resultados

# Esta función reutiliza un mismo formulario para la accion agregar o editar/eliminar
def agregar_o_editar_animal(modo, nombre, animal, edad, id, ventana):
    # Quito los espacios en blanco
    nombre = nombre.strip()
    animal = animal.strip()
    edad = edad.strip() 
    
    datos_validos = fn.validar_mascota(nombre, animal , edad, ventana)
    if datos_validos:
        if modo == 'Agregar': # Si se ejecuta en modo agregar mascota
            try :
                conexion = sql.connect("veterinariaDB")
                cursor = conexion.cursor()
                id_cliente = id
                datos = nombre, animal, int(edad), id_cliente
                cursor.execute('INSERT INTO mascotas values(NULL,?,?,?,?)', (datos))
                conexion.commit()
                print (cursor.fetchone())
                messagebox.showinfo("Agregar", "Mascota agregada con éxito", parent = ventana)
                conexion.close()
                ventana.destroy()
            except:
                messagebox.showwarning("Error", "No fue posible añadir la mascota", parent = ventana)
                conexion.close()

        elif modo == 'Editar':
            try :
                conexion = sql.connect("veterinariaDB")
                cursor = conexion.cursor()
                id_mascota = id
                
                cursor.execute(f"UPDATE mascotas SET nombre = '{nombre}', animal = '{animal}', edad = {edad} WHERE id_mascota = {id_mascota}")
                conexion.commit()
                
                messagebox.showinfo("Editar", "Mascota editada con éxito", parent = ventana)
                conexion.close()
                ventana.destroy()
            except :
                messagebox.showwarning("Error", "No fue posible editar la mascota", parent = ventana)
                conexion.close()
                


def buscar_mascota(id): # Busca en la base de datos la mascota a la que le hacemos doble ckick 
    try:
        conexion = sql.connect("veterinariaDB")
        cursor = conexion.cursor()
        cursor.execute(f"SELECT nombre, animal, edad FROM mascotas where id_mascota = {id} ")
        resultados = cursor.fetchone()
        conexion.close()
        return resultados

    except: 
        messagebox.showerror("Error", "Hubo un error a la hora de obtener los datos de la mascota")
        conexion.close()


def eliminar_mascota(id,ventana): # Elimina mascota
    try:
        conexion = sql.connect("veterinariaDB")
        cursor = conexion.cursor()
        cursor.execute(f"DELETE FROM mascotas WHERE id_mascota = {id}")
        conexion.commit()
        messagebox.showinfo("Eliminar mascota", "Mascota eliminada con exito", parent= ventana)
        conexion.close()
        ventana.destroy()

    except: 
        messagebox.showerror("Error", "No se pudo eliminar la mascota", parent = ventana)
        conexion.close()
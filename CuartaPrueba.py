import tkinter as tk
from tkinter import messagebox
import re  # Para las expresiones regulares

# Lista para almacenar los contactos
contactos = []

# Función para validar si el campo de nombre/apellidos contiene solo letras
def solo_letras(texto):
    return texto.isalpha()

# Función para validar si el campo de teléfono contiene solo números
def solo_numeros(texto):
    return texto.isdigit()

# Función para validar el correo
def es_correo_valido(correo):
    # Expresión regular básica para correo (debería mejorar para una validación más estricta)
    patron_correo = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(patron_correo, correo) is not None

# Función para agregar un contacto
def agregar_contacto():
    nombre = entry_nombre.get().strip()
    apellidos = entry_apellidos.get().strip()
    telefono = entry_telefono.get().strip()
    correo = entry_correo.get().strip()
    direccion = entry_direccion.get().strip()  # Cambié "ubicacion" a "direccion"
    
    # Validar que los campos no estén vacíos
    if not (nombre and apellidos and telefono and correo and direccion):
        messagebox.showerror("Error", "Por favor, completa todos los campos.")
        return
    
    # Validar que el nombre y apellidos solo contengan letras
    if not solo_letras(nombre) or not solo_letras(apellidos):
        messagebox.showerror("Error", "El nombre y los apellidos solo pueden contener letras.")
        return
    
    # Validar que el teléfono contenga solo números
    if not solo_numeros(telefono):
        messagebox.showerror("Error", "El teléfono solo puede contener números.")
        return
    
    # Validar que el correo tenga un formato válido
    if not es_correo_valido(correo):
        messagebox.showerror("Error", "Por favor, ingresa un correo electrónico válido.")
        return
    
    # Crear un contacto como diccionario
    contacto = {
        "nombre": nombre,
        "apellidos": apellidos,
        "telefono": telefono,
        "correo": correo,
        "direccion": direccion
    }
    
    # Agregar el contacto a la lista de contactos
    contactos.append(contacto)
    
    # Actualizar la lista de contactos mostrada
    actualizar_lista_contactos()

    # Limpiar los campos de entrada
    limpiar_campos()

# Función para eliminar un contacto seleccionado
def eliminar_contacto():
    # Obtener el índice del contacto seleccionado
    seleccionado = listbox_contactos.curselection()
    if not seleccionado:
        messagebox.showerror("Error", "Por favor, selecciona un contacto para eliminar.")
        return
    
    # Eliminar el contacto de la lista
    index = seleccionado[0]
    contactos.pop(index)
    
    # Actualizar la lista de contactos mostrada
    actualizar_lista_contactos()

# Función para actualizar la lista de contactos mostrados
def actualizar_lista_contactos():
    listbox_contactos.delete(0, tk.END)  # Limpiar la lista
    for contacto in contactos:
        listbox_contactos.insert(tk.END, f"{contacto['nombre']} {contacto['apellidos']}")

# Función para mostrar toda la información de un contacto seleccionado
def ver_informacion():
    seleccionado = listbox_contactos.curselection()
    if not seleccionado:
        messagebox.showerror("Error", "Por favor, selecciona un contacto para ver la información.")
        return

    # Obtener el índice del contacto seleccionado
    index = seleccionado[0]
    contacto = contactos[index]

    # Mostrar la información completa en los campos de texto
    label_info.config(text=f"Nombre: {contacto['nombre']}\nApellidos: {contacto['apellidos']}\n"
                          f"Teléfono: {contacto['telefono']}\nCorreo: {contacto['correo']}\n"
                          f"Dirección: {contacto['direccion']}")

# Función para editar la información de un contacto seleccionado
def editar_contacto():
    seleccionado = listbox_contactos.curselection()
    if not seleccionado:
        messagebox.showerror("Error", "Por favor, selecciona un contacto para editar.")
        return
    
    # Obtener el índice del contacto seleccionado
    index = seleccionado[0]
    contacto = contactos[index]

    # Rellenar los campos con la información del contacto seleccionado
    entry_nombre.delete(0, tk.END)
    entry_nombre.insert(0, contacto["nombre"])

    entry_apellidos.delete(0, tk.END)
    entry_apellidos.insert(0, contacto["apellidos"])

    entry_telefono.delete(0, tk.END)
    entry_telefono.insert(0, contacto["telefono"])

    entry_correo.delete(0, tk.END)
    entry_correo.insert(0, contacto["correo"])

    entry_direccion.delete(0, tk.END)
    entry_direccion.insert(0, contacto["direccion"])

    # Eliminar el contacto original para editarlo
    contactos.pop(index)

# Función para limpiar los campos de entrada
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_apellidos.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_direccion.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agenda de Contactos")

# Etiquetas y campos de entrada
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nombre = tk.Entry(ventana, width=30)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

label_apellidos = tk.Label(ventana, text="Apellidos:")
label_apellidos.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_apellidos = tk.Entry(ventana, width=30)
entry_apellidos.grid(row=1, column=1, padx=10, pady=5)

label_telefono = tk.Label(ventana, text="Teléfono (+34):")
label_telefono.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_telefono = tk.Entry(ventana, width=30)
entry_telefono.grid(row=2, column=1, padx=10, pady=5)
entry_telefono.insert(0, "+34")  # Teléfono predeterminado

label_correo = tk.Label(ventana, text="Correo (@gmail.com):")
label_correo.grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_correo = tk.Entry(ventana, width=30)
entry_correo.grid(row=3, column=1, padx=10, pady=5)
entry_correo.insert(0, "@gmail.com")  # Correo predeterminado

label_direccion = tk.Label(ventana, text="Dirección:")
label_direccion.grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_direccion = tk.Entry(ventana, width=30)
entry_direccion.grid(row=4, column=1, padx=10, pady=5)

# Botones
boton_agregar = tk.Button(ventana, text="Agregar Contacto", command=agregar_contacto)
boton_agregar.grid(row=5, column=0, columnspan=2, pady=10)

boton_eliminar = tk.Button(ventana, text="Eliminar Contacto", command=eliminar_contacto)
boton_eliminar.grid(row=6, column=0, columnspan=2, pady=10)

boton_ver_info = tk.Button(ventana, text="Ver Información", command=ver_informacion)
boton_ver_info.grid(row=7, column=0, columnspan=2, pady=10)

boton_editar = tk.Button(ventana, text="Editar Contacto", command=editar_contacto)
boton_editar.grid(row=8, column=0, columnspan=2, pady=10)

# Lista para mostrar los contactos
listbox_contactos = tk.Listbox(ventana, width=50, height=10)
listbox_contactos.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

# Etiqueta para mostrar la información completa del contacto seleccionado
label_info = tk.Label(ventana, text="", justify="left", font=("Arial", 10))
label_info.grid(row=10, column=0, columnspan=2, pady=10)

# Iniciar la interfaz
ventana.mainloop()

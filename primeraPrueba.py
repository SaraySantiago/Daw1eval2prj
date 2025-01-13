import tkinter as tk
from tkinter import messagebox

# Lista para almacenar los contactos
contactos = []

# Función para agregar un contacto
def agregar_contacto():
    nombre = entry_nombre.get().strip()
    apellidos = entry_apellidos.get().strip()
    telefono = entry_telefono.get().strip()
    correo = entry_correo.get().strip()
    ubicacion = entry_ubicacion.get().strip()
    
    # Validar si los campos están completos
    if not (nombre and apellidos and telefono and correo and ubicacion):
        messagebox.showerror("Error", "Por favor, completa todos los campos.")
        return
    
    # Crear un contacto como diccionario
    contacto = {
        "nombre": nombre,
        "apellidos": apellidos,
        "telefono": telefono,
        "correo": correo,
        "ubicacion": ubicacion
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

# Función para limpiar los campos de entrada
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_apellidos.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_ubicacion.delete(0, tk.END)

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

label_telefono = tk.Label(ventana, text="Teléfono:")
label_telefono.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_telefono = tk.Entry(ventana, width=30)
entry_telefono.grid(row=2, column=1, padx=10, pady=5)

label_correo = tk.Label(ventana, text="Correo:")
label_correo.grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_correo = tk.Entry(ventana, width=30)
entry_correo.grid(row=3, column=1, padx=10, pady=5)

label_ubicacion = tk.Label(ventana, text="Ubicación:")
label_ubicacion.grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_ubicacion = tk.Entry(ventana, width=30)
entry_ubicacion.grid(row=4, column=1, padx=10, pady=5)

# Botones
boton_agregar = tk.Button(ventana, text="Agregar Contacto", command=agregar_contacto)
boton_agregar.grid(row=5, column=0, columnspan=2, pady=10)

boton_eliminar = tk.Button(ventana, text="Eliminar Contacto", command=eliminar_contacto)
boton_eliminar.grid(row=6, column=0, columnspan=2, pady=10)

# Lista para mostrar los contactos
listbox_contactos = tk.Listbox(ventana, width=50, height=10)
listbox_contactos.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Iniciar la interfaz
ventana.mainloop()

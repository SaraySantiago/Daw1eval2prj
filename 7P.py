import tkinter as tk
from tkinter import messagebox
import re  # Para las expresiones regulares

# Clase Contacto (TDA)
class Contacto:
    def __init__(self, nombre, apellidos, telefono, correo, direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    # Método para validar que solo contenga letras (para nombre y apellidos)
    def solo_letras(self, texto):
        return texto.isalpha()

    # Método para validar que el teléfono contenga solo números y opcionalmente un "+"
    def es_telefono_valido(self, telefono):
        patron_telefono = r"^\+?\d+$"  # Permite un "+" al inicio seguido de números
        return re.match(patron_telefono, telefono) is not None

    # Método para validar que el correo tenga un formato válido
    def es_correo_valido(self, correo):
        patron_correo = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(patron_correo, correo) is not None

    # Método para validar todos los datos del contacto
    def es_valido(self):
        if not self.nombre or not self.apellidos or not self.telefono or not self.correo or not self.direccion:
            return False, "Por favor, completa todos los campos."

        if not self.solo_letras(self.nombre) or not self.solo_letras(self.apellidos):
            return False, "El nombre y los apellidos solo pueden contener letras."
        
        if not self.es_telefono_valido(self.telefono):
            return False, "El teléfono solo puede contener números y un '+' al inicio."
        
        if not self.es_correo_valido(self.correo):
            return False, "Por favor, ingresa un correo electrónico válido."
        
        return True, "Contacto válido."

# Lista para almacenar los contactos
contactos = []

# Función para agregar un contacto
def agregar_contacto(event=None):
    nombre = entry_nombre.get().strip()
    apellidos = entry_apellidos.get().strip()
    telefono = entry_telefono.get().strip()
    correo = entry_correo.get().strip()
    direccion = entry_direccion.get().strip()

    # Crear el objeto Contacto
    contacto = Contacto(nombre, apellidos, telefono, correo, direccion)

    # Validar el contacto
    es_valido, mensaje = contacto.es_valido()
    if not es_valido:
        messagebox.showerror("Error", mensaje)
        return
    
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
        listbox_contactos.insert(tk.END, f"{contacto.nombre} {contacto.apellidos}")

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
    label_info.config(text=f"Nombre: {contacto.nombre}\nApellidos: {contacto.apellidos}\n"
                          f"Teléfono: {contacto.telefono}\nCorreo: {contacto.correo}\n"
                          f"Dirección: {contacto.direccion}")

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
    entry_nombre.insert(0, contacto.nombre)

    entry_apellidos.delete(0, tk.END)
    entry_apellidos.insert(0, contacto.apellidos)

    entry_telefono.delete(0, tk.END)
    entry_telefono.insert(0, contacto.telefono)

    entry_correo.delete(0, tk.END)
    entry_correo.insert(0, contacto.correo)

    entry_direccion.delete(0, tk.END)
    entry_direccion.insert(0, contacto.direccion)

    # Eliminar el contacto original para editarlo
    contactos.pop(index)

# Función para limpiar los campos de entrada
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_apellidos.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_direccion.delete(0, tk.END)

# Función para confirmar salida
def confirmar_salida():
    respuesta = messagebox.askquestion("Salir", "¿Estás seguro de que quieres salir de tu agenda de contactos?")
    if respuesta == "yes":
        ventana.quit()

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

# Botones alineados horizontalmente
frame_botones = tk.Frame(ventana)
frame_botones.grid(row=5, column=0, columnspan=2, pady=10)

boton_agregar = tk.Button(frame_botones, text="Agregar Contacto", command=agregar_contacto)
boton_agregar.grid(row=0, column=0, padx=10)

boton_eliminar = tk.Button(frame_botones, text="Eliminar Contacto", command=eliminar_contacto)
boton_eliminar.grid(row=0, column=1, padx=10)

boton_ver_info = tk.Button(frame_botones, text="Ver Información", command=ver_informacion)
boton_ver_info.grid(row=0, column=2, padx=10)

boton_editar = tk.Button(frame_botones, text="Editar Contacto", command=editar_contacto)
boton_editar.grid(row=0, column=3, padx=10)

# Lista para mostrar los contactos
listbox_contactos = tk.Listbox(ventana, width=50, height=10)
listbox_contactos.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Etiqueta para mostrar la información completa del contacto seleccionado
label_info = tk.Label(ventana, text="", justify="left", font=("Arial", 10))
label_info.grid(row=7, column=0, columnspan=2, pady=10)

# Botón "Salir" en la parte inferior derecha
boton_salir = tk.Button(ventana, text="Salir", command=confirmar_salida)
boton_salir.grid(row=8, column=1, pady=10, sticky="e", padx=10)

# Asociar el evento de la tecla Enter para agregar un contacto
ventana.bind("<Return>", agregar_contacto)

# Iniciar la interfaz
ventana.mainloop()

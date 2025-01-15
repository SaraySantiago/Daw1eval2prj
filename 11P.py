import tkinter as tk
from tkinter import messagebox, Toplevel
import re  # Para las expresiones regulares

# Clase Contacto (TDA)
class Contacto:
    def __init__(self, nombre, primer_apellido, segundo_apellido, telefono, correo, direccion):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
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
        if not self.nombre or not self.primer_apellido or not self.telefono or not self.correo or not self.direccion:
            return False, "Por favor, completa todos los campos."

        if not self.solo_letras(self.nombre) or not self.solo_letras(self.primer_apellido):
            return False, "El nombre y el primer apellido solo pueden contener letras."
        
        if self.segundo_apellido and not self.solo_letras(self.segundo_apellido):
            return False, "El segundo apellido solo puede contener letras."
        
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
    primer_apellido = entry_primer_apellido.get().strip()
    segundo_apellido = entry_segundo_apellido.get().strip()
    telefono = entry_telefono.get().strip()
    correo = entry_correo.get().strip()
    direccion = entry_direccion.get().strip()

    # Crear el objeto Contacto
    contacto = Contacto(nombre, primer_apellido, segundo_apellido, telefono, correo, direccion)

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
        listbox_contactos.insert(tk.END, f"{contacto.nombre} {contacto.primer_apellido}")

# Función para mostrar la información de un contacto en una nueva ventana
def ver_informacion():
    seleccionado = listbox_contactos.curselection()
    if not seleccionado:
        messagebox.showerror("Error", "Por favor, selecciona un contacto para ver la información.")
        return

    # Obtener el índice del contacto seleccionado
    index = seleccionado[0]
    contacto = contactos[index]

    # Crear una nueva ventana para mostrar la información del contacto
    ventana_info = Toplevel(ventana)
    ventana_info.title("Información del Contacto")
    ventana_info.configure(bg="#FFB3B3")  # Fondo naranja pastel

    # Títulos de campos en negrita y con tamaño de fuente aumentado
    fuente_titulo = ("Montserrat", 12, "bold")
    fuente_texto = ("Arial", 10)

    # Mostrar la información del contacto de manera ordenada
    label_nombre = tk.Label(ventana_info, text=f"Nombre:", font=fuente_titulo, bg="#FFB3B3")
    label_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    label_nombre_info = tk.Label(ventana_info, text=contacto.nombre, font=fuente_texto, bg="#FFB3B3")
    label_nombre_info.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    label_primer_apellido = tk.Label(ventana_info, text=f"Primer Apellido:", font=fuente_titulo, bg="#FFB3B3")
    label_primer_apellido.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    label_primer_apellido_info = tk.Label(ventana_info, text=contacto.primer_apellido, font=fuente_texto, bg="#FFB3B3")
    label_primer_apellido_info.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    label_segundo_apellido = tk.Label(ventana_info, text=f"Segundo Apellido:", font=fuente_titulo, bg="#FFB3B3")
    label_segundo_apellido.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    label_segundo_apellido_info = tk.Label(ventana_info, text=contacto.segundo_apellido if contacto.segundo_apellido else 'No disponible', font=fuente_texto, bg="#FFB3B3")
    label_segundo_apellido_info.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    label_telefono = tk.Label(ventana_info, text=f"Teléfono:", font=fuente_titulo, bg="#FFB3B3")
    label_telefono.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    label_telefono_info = tk.Label(ventana_info, text=contacto.telefono, font=fuente_texto, bg="#FFB3B3")
    label_telefono_info.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    label_correo = tk.Label(ventana_info, text=f"Correo:", font=fuente_titulo, bg="#FFB3B3")
    label_correo.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    label_correo_info = tk.Label(ventana_info, text=contacto.correo, font=fuente_texto, bg="#FFB3B3")
    label_correo_info.grid(row=4, column=1, padx=10, pady=5, sticky="w")

    label_direccion = tk.Label(ventana_info, text=f"Dirección:", font=fuente_titulo, bg="#FFB3B3")
    label_direccion.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    label_direccion_info = tk.Label(ventana_info, text=contacto.direccion, font=fuente_texto, bg="#FFB3B3")
    label_direccion_info.grid(row=5, column=1, padx=10, pady=5, sticky="w")

    # Botón para cerrar la ventana de información
    boton_cerrar = tk.Button(ventana_info, text="Cerrar", command=ventana_info.destroy, font=("Montserrat", 10))
    boton_cerrar.grid(row=6, column=0, columnspan=2, pady=10)

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

    entry_primer_apellido.delete(0, tk.END)
    entry_primer_apellido.insert(0, contacto.primer_apellido)

    entry_segundo_apellido.delete(0, tk.END)
    entry_segundo_apellido.insert(0, contacto.segundo_apellido)

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
    entry_primer_apellido.delete(0, tk.END)
    entry_segundo_apellido.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_direccion.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agenda de Contactos")
ventana.configure(bg="#FFB3B3")  # Fondo naranja pastel

# Establecer la fuente y color de las etiquetas
fuente_etiquetas = ("Montserrat", 10, "bold")
fuente_campos = ("Arial", 10)
fuente_botones = ("Montserrat", 10)

# Etiquetas y campos de entrada
label_nombre = tk.Label(ventana, text="Nombre:", font=fuente_etiquetas, bg="#FFB3B3", fg="black")
label_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nombre = tk.Entry(ventana, width=30, font=fuente_campos, fg="#003366")
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

label_primer_apellido = tk.Label(ventana, text="Primer Apellido:", font=fuente_etiquetas, bg="#FFB3B3", fg="black")
label_primer_apellido.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_primer_apellido = tk.Entry(ventana, width=30, font=fuente_campos, fg="#003366")
entry_primer_apellido.grid(row=1, column=1, padx=10, pady=5)

label_segundo_apellido = tk.Label(ventana, text="Segundo Apellido:", font=fuente_etiquetas, bg="#FFB3B3", fg="black")
label_segundo_apellido.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_segundo_apellido = tk.Entry(ventana, width=30, font=fuente_campos, fg="#003366")
entry_segundo_apellido.grid(row=2, column=1, padx=10, pady=5)

label_telefono = tk.Label(ventana, text="Teléfono:", font=fuente_etiquetas, bg="#FFB3B3", fg="black")
label_telefono.grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_telefono = tk.Entry(ventana, width=30, font=fuente_campos, fg="#003366")
entry_telefono.grid(row=3, column=1, padx=10, pady=5)

label_correo = tk.Label(ventana, text="Correo:", font=fuente_etiquetas, bg="#FFB3B3", fg="black")
label_correo.grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_correo = tk.Entry(ventana, width=30, font=fuente_campos, fg="#003366")
entry_correo.grid(row=4, column=1, padx=10, pady=5)

label_direccion = tk.Label(ventana, text="Dirección:", font=fuente_etiquetas, bg="#FFB3B3", fg="black")
label_direccion.grid(row=5, column=0, padx=10, pady=5, sticky="e")
entry_direccion = tk.Entry(ventana, width=30, font=fuente_campos, fg="#003366")
entry_direccion.grid(row=5, column=1, padx=10, pady=5)

# Botones alineados horizontalmente
frame_botones = tk.Frame(ventana, bg="#FFB3B3")
frame_botones.grid(row=6, column=0, columnspan=2, pady=10)

boton_agregar = tk.Button(frame_botones, text="Agregar Contacto", command=agregar_contacto, font=fuente_botones)
boton_agregar.grid(row=0, column=0, padx=10)

boton_eliminar = tk.Button(frame_botones, text="Eliminar Contacto", command=eliminar_contacto, font=fuente_botones)
boton_eliminar.grid(row=0, column=1, padx=10)

boton_ver_info = tk.Button(frame_botones, text="Ver Información", command=ver_informacion, font=fuente_botones)
boton_ver_info.grid(row=0, column=2, padx=10)

boton_editar = tk.Button(frame_botones, text="Editar Contacto", command=editar_contacto, font=fuente_botones)
boton_editar.grid(row=0, column=3, padx=10)

# Lista para mostrar los contactos
listbox_contactos = tk.Listbox(ventana, width=50, height=10, font=fuente_campos)
listbox_contactos.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Botón "Salir" en la parte inferior derecha
boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit, font=fuente_botones)
boton_salir.grid(row=8, column=1, pady=10, sticky="e", padx=10)

# Iniciar la interfaz
ventana.mainloop()

import tkinter as tk
import json

with open('errores.json','r') as file:
    data = json.load(file)

def obtenerDesc():
    print("Hola")
#Crear ventana del programa
ventana = tk.Tk() #crear pantalla
ventana.title("Scanner OBD")
# ventana.geometry("500x300")
ventana.resizable(0,0)

#mensaje
codigo = tk.Label(ventana, text= "Ingrese el codigo de error:")
codigo.pack(pady=10, padx=10)
#cuadro de texto
codigo_entry = tk.Entry(ventana)
codigo_entry.pack(pady=10, padx=10)
#boton
buscar_btn = tk.Button(ventana, text="Buscar error", command=obtenerDesc)
buscar_btn.pack(pady=10, padx=10)

descripcion = tk.Label(ventana, text="")
descripcion.pack()

ventana.mainloop() #mantendra ventana abierta


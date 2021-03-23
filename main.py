import manejador
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk

# manejador.cargarArchivo("PYTHON\\2021_1S\\IPC2_Proyecto2_201709020\\entrada.xml")
# manejador.generaImagen()
# manejador.generaImagen()


ventana = tk.Tk()
ventana.title("Proyecto 2 - IPC2")
ventana.geometry("700x500") #tamaño ventana

tabs = ttk.Notebook(ventana)

#CARGAR ARCHIVO
load = ttk.Frame(tabs)
#elementos
ca_lbl = ttk.Label(load, text="Archivo Cargado:",width=16) #Crea un label
ca_lbl.pack(side = tk.LEFT, padx=10, pady=5) #Agrega a la ventana
# ca_txt = ttk.Label(load, text="Ninguno...", background="white",width=50)
# ca_txt.pack(side = tk.LEFT, fill = tk.X, expand=True, padx=10, pady=5)
ca_txt = ttk.Entry(load, text="Ninguno...", background="white",width=50, state=False)
ca_txt.pack(side = tk.LEFT, fill = tk.X, expand=True, padx=10, pady=5)
def cargarArchivo():
    file = filedialog.askopenfilename(title="Selecciona un archivo", filetypes=[("xml files", "*.xml")])
    ca_txt["text"]=file
    if file:
        manejador.cargarArchivo(file)
        print("archivo", file)

ca_btn = ttk.Button(load, text = "Abrir Archivo", width=13, command=cargarArchivo)
ca_btn.pack(side = tk.RIGHT, padx=10, pady=5)
tabs.add(load, text="Cargar Archivo", padding=10)

#OPERACIONES
oprtsn = ttk.Frame(tabs)
#elementos
opr_lbl = ttk.Label(oprtsn, text="Elige la operación a mostrar") #Crea un label
opr_lbl.pack(padx=10, pady=5) #Agrega a la ventana

opr_lbl2 = ttk.Label(oprtsn, text="Una imagen a operar") #Crea un label
opr_lbl2.pack(padx=10, pady=5) #Agrega a la ventana

tabs.add(oprtsn, text="Operaciones", padding=10)

tabs.pack(fill=tk.X)
#ventana.pack()

ventana.mainloop()

import manejador
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk

# manejador.cargarArchivo("PYTHON\\2021_1S\\IPC2_Proyecto2_201709020\\entrada.xml")
# manejador.generaImagen()
# manejador.generaImagen()


ventana = tk.Tk()
ventana.title("Proyecto 2 - IPC2")
ventana.geometry("900x600") #tamaño ventana

tabs = ttk.Notebook(ventana)

#PANELES
img = tk.PhotoImage(file="PYTHON\\2021_1S\\IPC2_Proyecto2_201709020\\img_original-grafo.png")
img2 = tk.PhotoImage(file="PYTHON\\2021_1S\\IPC2_Proyecto2_201709020\\img_modificada-grafo.png")
img = img.subsample(3,3)
img2 = img2.subsample(3,3)
panel1 = tk.Label(ventana, image=img, width = 430, height = 430)
panel2 = tk.Label(ventana, image=img2, width = 430, height = 430)

#OPERACIONES --------------------------------------------------------------------------------------------
oprtsn = ttk.Frame(tabs)
#elementos
opr_lbl = ttk.Label(oprtsn, text="Generar ") #Crea un label
opr_cmbx = ttk.Combobox(oprtsn, state="readonly")
opr_cmbx["values"]=["Rot. Horizontal", "Rot. Vertical", "Transpuesta"]

opr_lbl2 = ttk.Label(oprtsn, text="De la imagen ") #Crea un label
opr_cmbx2 = ttk.Combobox(oprtsn, state="readonly")
def visualizar():
    sel1 = opr_cmbx.get()
    sel2 = opr_cmbx2.get()
    if sel1 and sel2:
        if sel1 == "Rot. Horizontal":
            manejador.generaImagen(sel2,"h")
        elif sel1 == "Rot. Vertical":
            manejador.generaImagen(sel2,"v")
        else:
            manejador.generaImagen(sel2,"t")
        print("Operacion:", sel1, " sobre la img:", sel2)
        img3 = tk.PhotoImage(file="PYTHON\\2021_1S\\IPC2_Proyecto2_201709020\\img_original-grafo.png")
        img4 = tk.PhotoImage(file="PYTHON\\2021_1S\\IPC2_Proyecto2_201709020\\img_modificada-grafo.png")
        img3 = img3.subsample(3,3)
        img4 = img4.subsample(3,3)
        global panel1, panel2
        panel1.configure(image=img3)
        panel2.configure(image=img4)
        panel1.image=img3
        panel2.image=img4
    else:
        print("Faltan datos")
opr_btn = ttk.Button(oprtsn, text = "Visualizar", width=13, command=visualizar)

#CARGAR ARCHIVO -------------------------------------------------------------------------------------------
load = ttk.Frame(tabs)
#elementos
ca_lbl = ttk.Label(load, text="Archivo Cargado:",width=16) #Crea un label
# ca_txt = ttk.Label(load, text="Ninguno...", background="white",width=50)
# ca_txt.pack(side = tk.LEFT, fill = tk.X, expand=True, padx=10, pady=5)
ca_txt = ttk.Entry(load,width=50)
ca_txt.insert(0, "No hay ningun archivo cargado...")
def cargarArchivo():
    file = filedialog.askopenfilename(title="Selecciona un archivo", filetypes=[("xml files", "*.xml")])
    if file:
        ca_txt.delete(0, tk.END)
        ca_txt.insert(0, str(file))
        manejador.cargarArchivo(file)
        opr_cmbx2["values"]=manejador.listaImagenes()
        # print("archivo", file)

ca_btn = ttk.Button(load, text = "Abrir Archivo", width=13, command=cargarArchivo)

#Creando las pestañas ------------------------------------------------------------------------------------
tabs.add(load, text="Cargar Archivo", padding=10)
tabs.add(oprtsn, text="Operaciones Básicas", padding=10)

#Añadiendo los elementos a los paneles de las pestañas ---------------------------------------------------
ca_lbl.pack(side = tk.LEFT, padx=10, pady=5)
ca_txt.pack(side = tk.LEFT, fill = tk.X, expand=True, padx=10, pady=5)
ca_btn.pack(side = tk.RIGHT, padx=10, pady=5)
opr_lbl.pack(side = tk.LEFT, padx=10, pady=5)
opr_cmbx.pack(side = tk.LEFT, padx=10, pady=5)
opr_lbl2.pack(side = tk.LEFT, padx=10, pady=5)
opr_cmbx2.pack(side = tk.LEFT, padx=10, pady=5)
opr_btn.pack(side = tk.RIGHT, padx=10, pady=5)

tabs.pack(fill=tk.X)

panel1.pack(side = tk.LEFT)
panel2.pack(side = tk.RIGHT)

ventana.mainloop()

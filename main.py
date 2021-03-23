import manejador
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk

# manejador.cargarArchivo("PYTHON\\2021_1S\\IPC2_Proyecto2_201709020\\entrada.xml")
# manejador.generaImagen()
# manejador.generaImagen()

def dameReduccion(dim1, dim2):
    de1 = dim1//530
    de2 = dim2//530
    dd1 = dim1/530
    dd2 = dim2/530
    print("Enteros:", de1, de2, " Decimales:", dd1, dd2)
    if de1 >= de2:
        if (float(de1)+0.50) >= dd1:
        # if float(de1) >= dd1:
            return de1
        else:
            return de1+1
    else:
        if (float(de2)+0.50) >= dd2:
        # if float(de2) >= dd2:
            return de2
        else:
            return de2+1

ventana = tk.Tk()
ventana.title("Proyecto 2 - IPC2")
ventana.geometry("1160x680") #tamaño ventana
# mygreen = "#d2ffd2"
# myred = "#dd0202"

# style = ttk.Style()

# style.theme_create( "yummy", parent="alt", settings={
#         "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
#         "TNotebook.Tab": {
#             "configure": {"padding": [5, 1], "background": mygreen },
#             "map":       {"background": [("selected", myred)],
#                           "expand": [("selected", [1, 1, 1, 0])] } } } )

# style.theme_use("yummy")

tabs = ttk.Notebook(ventana)

#PANELES
pan_vista1 = ttk.Frame(ventana)
pan_vista2 = ttk.Frame(ventana)
img = tk.PhotoImage(file="PYTHON\\2021_1S\\IPC2_Proyecto2_201709020\\default.png")
img2 = tk.PhotoImage(file="PYTHON\\2021_1S\\IPC2_Proyecto2_201709020\\default.png")
# img = img.subsample(2,2)
# img2 = img2.subsample(2,2)
panel1 = tk.Label(pan_vista1, image=img, width = 575, height = 530, background="gray")
panel2 = tk.Label(pan_vista2, image=img2, width = 575, height = 530, background="black")

info1 = tk.Label(pan_vista1, text="MATRIZ ORIGINAL", background="red")
info2 = tk.Label(pan_vista2, text="MATRIZ MODIFICADA", background="orange")

#OPERACIONES --------------------------------------------------------------------------------------------
oprtsn = ttk.Frame(tabs)
#elementos
opr_lbl = ttk.Label(oprtsn, text="Generar ") #Crea un label
opr_cmbx = ttk.Combobox(oprtsn, state="readonly")
opr_cmbx["values"]=["Rot. Horizontal", "Rot. Vertical", "Transpuesta"]

opr_lbl2 = ttk.Label(oprtsn, text="De la imagen ") #Crea un label
opr_cmbx2 = ttk.Combobox(oprtsn, state="readonly")
def recargar():
    img3 = tk.PhotoImage(file="PYTHON\\2021_1S\\IPC2_Proyecto2_201709020\\img_original-grafo.png")
    img4 = tk.PhotoImage(file="PYTHON\\2021_1S\\IPC2_Proyecto2_201709020\\img_modificada-grafo.png")
    reduc = dameReduccion(img3.height(),img3.width())
    #print("REDUCCION ----------------------------------", reduc)
    img3 = img3.subsample(reduc,reduc)
    img4 = img4.subsample(reduc,reduc)
    global panel1, panel2
    panel1.configure(image=img3)
    panel2.configure(image=img4)
    panel1.image=img3
    panel2.image=img4
opr_btn2 = ttk.Button(oprtsn, text = "Recargar", width=13, command=recargar, state=tk.DISABLED)
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
        reduc = dameReduccion(img3.height(),img3.width())
        print("REDUCCION ----------------------------------", reduc)
        img3 = img3.subsample(reduc,reduc)
        img4 = img4.subsample(reduc,reduc)
        global panel1, panel2, opr_btn2
        panel1.configure(image=img3)
        panel2.configure(image=img4)
        panel1.image=img3
        panel2.image=img4
        opr_btn2["state"]=tk.ACTIVE
        opr_btn2.state=tk.ACTIVE
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
opr_btn.pack(side = tk.LEFT, padx=10, pady=5)
opr_btn2.pack(side = tk.LEFT, padx=10, pady=5)

tabs.pack(fill=tk.X)

panel1.pack(side = tk.TOP)
info1.pack(side = tk.BOTTOM, fill = tk.BOTH, expand=True)
panel2.pack(side = tk.TOP)
info2.pack(side = tk.BOTTOM, fill = tk.BOTH, expand=True)

pan_vista1.pack(side = tk.LEFT)
pan_vista2.pack(side = tk.RIGHT)

ventana.mainloop()

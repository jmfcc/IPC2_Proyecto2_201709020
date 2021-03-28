import manejador
from tkinter import filedialog
import tkinter as tk
from os import path
from tkinter import ttk

def getSource():
    ruta = path.dirname(path.abspath(__file__)) #Obtiene la ruta del script en ejecución
    return ruta

def dameReduccion(dim1, dim2):
    de1 = dim1//530
    de2 = dim2//530
    dd1 = dim1/530
    dd2 = dim2/530
    print("Enteros:", de1, de2, " Decimales:", dd1, dd2)
    if de1 >= de2:
        if (float(de1)+0.50) >= dd1:
        # if float(de1) >= dd1:
            if de1 == 0:
                de1 += 1
            return de1
        else:
            return de1+1
    else:
        if (float(de2)+0.50) >= dd2:
        # if float(de2) >= dd2:
            if de2 == 0:
                de2 += 1
            return de2
        else:
            return de2+1

ventana = tk.Tk()
ventana.title("Proyecto 2 - IPC2")
ventana.geometry("1160x640") #tamaño ventana

tabs = ttk.Notebook(ventana)

#PANELES
pan_vista1 = ttk.Frame(ventana)
pan_vista2 = ttk.Frame(ventana)
ruta = getSource()
img = tk.PhotoImage(file= ruta+"\\src\\default\\default1.png")
img2 = tk.PhotoImage(file=ruta+"\\src\\default\\default2.png")
# img = img.subsample(2,2)
# img2 = img2.subsample(2,2)
panel1 = tk.Label(pan_vista1, image=img, width = 575, height = 530, background="gray")
panel2 = tk.Label(pan_vista2, image=img2, width = 575, height = 530, background="black")

info1 = tk.Label(pan_vista1, text="MATRIZ ORIGINAL", background="red")
info2 = tk.Label(pan_vista2, text="MATRIZ MODIFICADA", background="orange")

#OPERACIONES BASICAS --------------------------------------------------------------------------------------------
oprtsn = ttk.Frame(tabs)
#elementos
opr_lbl = ttk.Label(oprtsn, text="Generar ") #Crea un label
opr_cmbx = ttk.Combobox(oprtsn, state="readonly")
opr_cmbx["values"]=["Rot. Horizontal", "Rot. Vertical", "Transpuesta"]

opr_lbl2 = ttk.Label(oprtsn, text="De la imagen ") #Crea un label
opr_cmbx2 = ttk.Combobox(oprtsn, state="readonly")

def muestraOriginal():
    sel2 = opr_cmbx2.get()
    if sel2:
        manejador.generaImagenO(sel2)
        ruta = getSource()
        img3 = tk.PhotoImage(file= ruta+"\\src\\imgs\\img_original-grafo.png")
        img4 = tk.PhotoImage(file= ruta+"\\src\\default\\default2.png")
        reduc = dameReduccion(img3.height(),img3.width())
        #print("REDUCCION ----------------------------------", reduc)
        img3 = img3.subsample(reduc,reduc)
        global panel1, panel2
        panel1.configure(image=img3)
        panel1.image=img3
        panel2.configure(image=img4)
        panel2.image=img4

opr_btn2 = ttk.Button(oprtsn, text = "Mostrar Matriz", width=15, command=muestraOriginal)

def visualizar():
    sel1 = opr_cmbx.get()
    sel2 = opr_cmbx2.get()
    if sel1 and sel2:
        manejador.generaImagenO(sel2)
        if sel1 == "Rot. Horizontal":
            manejador.generaImagenMod(sel2,"h", sel1)
        elif sel1 == "Rot. Vertical":
            manejador.generaImagenMod(sel2,"v", sel1)
        else:
            manejador.generaImagenMod(sel2,"t", sel1)
        #print("Operacion:", sel1, " sobre la img:", sel2)
        ruta = getSource()
        img3 = tk.PhotoImage(file= ruta+"\\src\\imgs\\img_original-grafo.png")
        img4 = tk.PhotoImage(file= ruta+"\\src\\imgs\\img_modificada-grafo.png")
        reduc = dameReduccion(img3.height(),img3.width())
        #print("REDUCCION ----------------------------------", reduc)
        img3 = img3.subsample(reduc,reduc)
        img4 = img4.subsample(reduc,reduc)
        global panel1, panel2, opr_btn2
        panel1.configure(image=img3)
        panel2.configure(image=img4)
        panel1.image=img3
        panel2.image=img4
        opr_btn2["state"]=tk.ACTIVE
        opr_btn2.state=tk.ACTIVE
        defaultOpEd1()
        defaultOpEd2()
        defaultOpEd()
        opLogicClear()
    else:
        print("Faltan datos")

opr_btn = ttk.Button(oprtsn, text = "Realizar Operación", width=18, command=visualizar)

#OPERACIONES DE EDICIÓN--------------------------------------------------------------------------------------------
opredit = ttk.Frame(tabs)
#elementos
opredit_lbl4 = ttk.Label(opredit, text="-----") #Crea un label
opredit_cmbx4 = ttk.Combobox(opredit, width=5, state=tk.DISABLED)
opredit_lbl6 = ttk.Label(opredit, text="-----") #Crea un label
opredit_cmbx6 = ttk.Combobox(opredit, width=5, state=tk.DISABLED)

def habilitaSecundarioF(event):
    modoEdicion = opredit_cmbx2.get()
    dim_Img = manejador.tamanioImagen(opredit_cmbx.get())
    opredit_cmbx4.set("")
    if modoEdicion == "Limpiar área" or modoEdicion == "Linea Vert.":
        filas = [x+1 for x in range(int(opredit_cmbx3.get())-1, dim_Img[0])]
        #Posteriores
        opredit_cmbx4["values"]=filas
        opredit_cmbx4["state"]="readonly"

    elif modoEdicion == "Linea Horiz.":
        pass

    elif modoEdicion == "Rectángulo":
        filas = [x+1 for x in range(0, dim_Img[0]-int(opredit_cmbx3.get())+1)]
        #Posteriores
        opredit_cmbx4["values"]=filas
        opredit_cmbx4["state"]="readonly"

    elif modoEdicion == "Triángulo":
        f = int(opredit_cmbx3.get())
        c = opredit_cmbx5.get()
        cols = [x+1 for x in range(0, dim_Img[0]-f + 1)]
        if c:
            opredit_cmbx6.set("")
            f = dim_Img[0] - int(opredit_cmbx3.get())
            c = dim_Img[1] - int(opredit_cmbx5.get())
            if f > c:
                c = int(opredit_cmbx5.get())
                cols = [x+1 for x in range(0, dim_Img[1]-c + 1)]
            #Posteriores
            opredit_cmbx6["values"]=cols
            opredit_cmbx6["state"]="readonly"

def habilitaSecundarioC(event):
    modoEdicion = opredit_cmbx2.get()
    dim_Img = manejador.tamanioImagen(opredit_cmbx.get())
    opredit_cmbx6.set("")
    if modoEdicion == "Limpiar área" or modoEdicion == "Linea Horiz.":
        cols = [x+1 for x in range(int(opredit_cmbx5.get())-1, dim_Img[1])]
        #Posteriores
        opredit_cmbx6["values"]=cols
        opredit_cmbx6["state"]="readonly"

    elif modoEdicion == "Linea Vert.":
        pass

    elif modoEdicion == "Rectángulo":
        cols = [x+1 for x in range(0, dim_Img[1] - int(opredit_cmbx5.get()) + 1)]
        #Posteriores
        opredit_cmbx6["values"]=cols
        opredit_cmbx6["state"]="readonly"

    elif modoEdicion == "Triángulo":
        c = int(opredit_cmbx5.get())
        f = opredit_cmbx3.get()
        cols = [x+1 for x in range(0, dim_Img[1]-c + 1)]
        if f:
            f = dim_Img[0] - int(opredit_cmbx3.get())
            c = dim_Img[1] - int(opredit_cmbx5.get())
            if f < c:
                f = int(opredit_cmbx3.get())
                cols = [x+1 for x in range(0, dim_Img[0]-f + 1)]
            #Posteriores
            opredit_cmbx6["values"]=cols
            opredit_cmbx6["state"]="readonly"

opredit_lbl3 = ttk.Label(opredit, text="-----") #Crea un label
opredit_cmbx3 = ttk.Combobox(opredit, width=5, state=tk.DISABLED)
opredit_cmbx3.bind("<<ComboboxSelected>>", habilitaSecundarioF)
opredit_lbl5 = ttk.Label(opredit, text="-----") #Crea un label
opredit_cmbx5 = ttk.Combobox(opredit, width=5, state=tk.DISABLED)
opredit_cmbx5.bind("<<ComboboxSelected>>", habilitaSecundarioC)

def habilitaEntradas(event):
    modoEdicion = opredit_cmbx2.get()
    dim_Img = manejador.tamanioImagen(opredit_cmbx.get())
    filas = [x+1 for x in range(0, dim_Img[0])]
    cols = [x+1 for x in range(0, dim_Img[1])]
    #print(filas, cols)
    defaultOpEd2()
    defaultOpEd()
    if modoEdicion == "Limpiar área":
        opredit_lbl3["text"]="Fila Inic."
        opredit_cmbx3["values"]=filas
        opredit_cmbx3["state"]="readonly"
        opredit_lbl5["text"]="Col. Inic."
        opredit_cmbx5["values"]=cols
        opredit_cmbx5["state"]="readonly"
        #Posteriores
        opredit_lbl4["text"]="Fila Fin"
        opredit_lbl6["text"]="Col. Fin"
    
    elif modoEdicion == "Linea Horiz.":
        opredit_lbl3["text"]="Fila"
        opredit_cmbx3["values"]=filas
        opredit_cmbx3["state"]="readonly"
        opredit_lbl5["text"]="Col. Inic."
        opredit_cmbx5["values"]=cols
        opredit_cmbx5["state"]="readonly"
        #Posteriores
        opredit_lbl6["text"]="Col. Fin"

    elif modoEdicion == "Linea Vert.":
        opredit_lbl3["text"]="Fila Inic."
        opredit_cmbx3["values"]=filas
        opredit_cmbx3["state"]="readonly"
        opredit_lbl5["text"]="Columna"
        opredit_cmbx5["values"]=cols
        opredit_cmbx5["state"]="readonly"
        #Posteriores
        opredit_lbl4["text"]="Fila Fin"

    elif modoEdicion == "Rectángulo":
        opredit_lbl3["text"]="Fila Inic."
        opredit_cmbx3["values"]=filas
        opredit_cmbx3["state"]="readonly"
        opredit_lbl5["text"]="Col. Inic."
        opredit_cmbx5["values"]=cols
        opredit_cmbx5["state"]="readonly"
        #Posteriores
        opredit_lbl4["text"]="Alto"
        opredit_lbl6["text"]="Ancho"

    elif modoEdicion == "Triángulo":
        opredit_lbl3["text"]="Fila Inic."
        opredit_cmbx3["values"]=filas
        opredit_cmbx3["state"]="readonly"
        opredit_lbl5["text"]="Col. Inic."
        opredit_cmbx5["values"]=cols
        opredit_cmbx5["state"]="readonly"
        #Posteriores
        opredit_lbl6["text"]="Tamaño"

opredit_lbl2 = ttk.Label(opredit, text="Edición:") #Crea un label
opredit_cmbx2 = ttk.Combobox(opredit, width=10, state=tk.DISABLED)
opredit_cmbx2["values"]=["Limpiar área", "Linea Horiz.", "Linea Vert.", "Rectángulo", "Triángulo"]
opredit_cmbx2.bind("<<ComboboxSelected>>", habilitaEntradas)

def habilitaEdit(event):
    # print(opredit_cmbx.get())
    defaultOpEd1()
    defaultOpEd2()
    defaultOpEd()
    opredit_cmbx2["state"]="readonly"

opredit_lbl = ttk.Label(opredit, text="Imagen:") #Crea un label
opredit_cmbx = ttk.Combobox(opredit,  width=10, state="readonly")
opredit_cmbx.bind("<<ComboboxSelected>>", habilitaEdit)
# opredit_cmbx["values"]=["Rot. Horizontal", "Rot. Vertical", "Transpuesta"]

def visualizarOE():
    sel1 = opredit_cmbx.get()
    if sel1:
        ruta = getSource()
        img3 = tk.PhotoImage(file= ruta+"\\src\\imgs\\img_original-grafo.png")
        img4 = tk.PhotoImage(file= ruta+"\\src\\imgs\\img_modificada-grafo.png")
        reduc = dameReduccion(img3.height(),img3.width())
        img3 = img3.subsample(reduc,reduc)
        img4 = img4.subsample(reduc,reduc)
        global panel1, panel2
        panel1.configure(image=img3)
        panel2.configure(image=img4)
        panel1.image=img3
        panel2.image=img4
    else:
        print("Faltan datos")

def editaImagen():                  #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    modoEdicion = opredit_cmbx2.get()
    sel1 = opredit_cmbx.get() #Img
    sel2 = opredit_cmbx2.get()#Tipo-Edicion
    if sel1 and sel2:
        sel3 = opredit_cmbx3.get()#F1
        sel4 = opredit_cmbx4.get()#F2
        sel5 = opredit_cmbx5.get()#C1
        sel6 = opredit_cmbx6.get()#C2
        if modoEdicion == "Limpiar área":
            if sel3 and sel4 and sel5 and sel6:
                manejador.generaImagenO(sel1)
                manejador.operationEdit(sel1, sel2, [int(sel3), int(sel4), int(sel5), int(sel6)])
                visualizarOE()
        elif modoEdicion == "Linea Horiz.":
            if sel3 and sel5 and sel6:
                manejador.generaImagenO(sel1)
                manejador.operationEdit(sel1, sel2, [int(sel3), int(sel5), int(sel6)])
                visualizarOE()
        elif modoEdicion == "Linea Vert.":
            if sel3 and sel4 and sel5:
                manejador.generaImagenO(sel1)
                manejador.operationEdit(sel1, sel2, [int(sel3), int(sel4), int(sel5)])
                visualizarOE()
        elif modoEdicion == "Rectángulo":
            if sel3 and sel4 and sel5 and sel6:
                manejador.generaImagenO(sel1)
                manejador.operationEdit(sel1, sel2, [int(sel3), int(sel4), int(sel5), int(sel6)])
                visualizarOE()
        elif modoEdicion == "Triángulo":
            if sel3 and sel5 and sel6:
                manejador.generaImagenO(sel1)
                manejador.operationEdit(sel1, sel2, [int(sel3), int(sel5), int(sel6)])
                visualizarOE()

opredit_btn2 = ttk.Button(opredit, text = "Recargar", width=13, command=None, state=tk.DISABLED)
opredit_btn = ttk.Button(opredit, text = "Realizar Edición", width=15, command=editaImagen)

def defaultOpEd1():
    opredit_cmbx2.set("")
    opredit_cmbx2["state"]=tk.DISABLED
def defaultOpEd2():
    opredit_lbl3["text"]="-----"
    opredit_cmbx3.set("")
    opredit_cmbx3["state"]=tk.DISABLED
    opredit_lbl5["text"]="-----"
    opredit_cmbx5.set("")
    opredit_cmbx5["state"]=tk.DISABLED
def defaultOpEd():
    opredit_lbl4["text"]="-----"
    opredit_cmbx4.set("")
    opredit_cmbx4["state"]=tk.DISABLED
    opredit_lbl6["text"]="-----"
    opredit_cmbx6.set("")
    opredit_cmbx6["state"]=tk.DISABLED

#OPERACIONES LOGICAS --------------------------------------------------------------------------------------------
oprlog = ttk.Frame(tabs)
#elementos
oprlog_lbl3 = ttk.Label(oprlog, text="Imagen 2:") #Crea un label
oprlog_cmbx3 = ttk.Combobox(oprlog, state=tk.DISABLED)

oprlog_lbl = ttk.Label(oprlog, text="Operación:") #Crea un label
oprlog_cmbx = ttk.Combobox(oprlog, state=tk.DISABLED)
oprlog_cmbx["values"]=["Unión", "Intersección", "Diferencia", "Diferencia Simétrica"]

def creaListaImg(event):
    seleccion = oprlog_cmbx2.get()
    nuevaLista = manejador.getLista().filtroDimensiones(seleccion)
    nuevaLista.remove(seleccion)
    oprlog_cmbx3.set("")
    oprlog_cmbx.set("")
    if nuevaLista:
        oprlog_cmbx3["values"]=nuevaLista
        oprlog_cmbx["state"]="readonly"
        oprlog_cmbx3["state"]="readonly"
    else:
        oprlog_cmbx["state"]=tk.DISABLED
        oprlog_cmbx3["state"]=tk.DISABLED

oprlog_lbl2 = ttk.Label(oprlog, text="Imagen 1:") #Crea un label
oprlog_cmbx2 = ttk.Combobox(oprlog, state="readonly")
oprlog_cmbx2.bind("<<ComboboxSelected>>", creaListaImg)

imagenOpLog = None
entradaNV = None
textLblOpLog = ""
def guardaImagenOpLog():
    global imagenOpLog, entradaNV
    nombreOpLog = entradaNV.get()
    if imagenOpLog != None and nombreOpLog:
        manejador.agregaImagenOpLog(nombreOpLog, imagenOpLog.getFilas(), imagenOpLog.getColumnas(), imagenOpLog.getImagen())
        print("se almacena con el nombre", nombreOpLog)
        actualizaListas()
        opLogicClear()
    else:
        print("No hay nombre a almacenar")

def creaNuevaVentana():
    global entradaNV, textLblOpLog
    nuevaVentana = tk.Toplevel(ventana)
    nuevaVentana.title("Operación Logica entre Imágenes")
    nuevaVentana.geometry('590x585')
    pan_New2 = ttk.Frame(nuevaVentana)
    lblNV = ttk.Label(pan_New2, text="Nombre de matriz")
    entradaNV = ttk.Entry(pan_New2)
    buttonNV = ttk.Button(pan_New2, text="Guardar Imagen", command= guardaImagenOpLog)
    pan_New = ttk.Frame(nuevaVentana)
    img = tk.PhotoImage(file= ruta+"\\src\\imgs\\img_opLogic-grafo.png")
    reduc = dameReduccion(img.height(),img.width())
    img = img.subsample(reduc,reduc)
    panelN = tk.Label(pan_New, image=img, width = 575, height = 530, background="gray")
    infoN = tk.Label(pan_New, text=textLblOpLog, background="green")
    panelN.pack(side=tk.TOP)
    infoN.pack(side=tk.BOTTOM, fill = tk.BOTH, expand=True)
    lblNV.pack(side=tk.LEFT)
    entradaNV.pack(side=tk.LEFT)
    buttonNV.pack(side=tk.LEFT)
    pan_New.pack(side=tk.TOP)
    pan_New2.pack(side=tk.BOTTOM)
    nuevaVentana.grab_set()
    ventana.wait_window(nuevaVentana)

def visualizarOriginalesLogic():
    ruta = getSource()
    img3 = tk.PhotoImage(file= ruta+"\\src\\imgs\\img_original-grafo.png")
    img4 = tk.PhotoImage(file= ruta+"\\src\\imgs\\img_original2-grafo.png")
    reduc = dameReduccion(img3.height(),img3.width())
    img3 = img3.subsample(reduc,reduc)
    img4 = img4.subsample(reduc,reduc)
    global panel1, panel2
    panel1.configure(image=img3)
    panel2.configure(image=img4)
    panel1.image=img3
    panel2.image=img4
    creaNuevaVentana()

def operacionLogica():
    sel1 = oprlog_cmbx2.get()
    sel2 = oprlog_cmbx3.get()
    opr_log = oprlog_cmbx.get()
    if sel1 and sel2 and opr_log:
        global textLblOpLog
        textLblOpLog = sel1 + " " + opr_log + " " + sel2
        manejador.generaImagenO(sel1)
        manejador.generaImagenO2(sel2)
        global imagenOpLog
        if opr_log == "Unión":
            imagenOpLog = manejador.union(sel1, sel2)
        elif opr_log == "Intersección":
            imagenOpLog = manejador.interseccion(sel1, sel2)
        elif opr_log == "Diferencia":
            imagenOpLog = manejador.diferencia(sel1, sel2)
        elif opr_log == "Diferencia Simétrica":
            imagenOpLog = manejador.diferenciaSimetrica(sel1, sel2)
        visualizarOriginalesLogic()

oprlog_btn2 = ttk.Button(oprlog, text = "Mostrar Matriz", width=15, command=None)
oprlog_btn = ttk.Button(oprlog, text = "Realizar Operación", width=18, command=operacionLogica)

def opLogicClear():
    oprlog_cmbx2.set("")
    oprlog_cmbx.set("")
    oprlog_cmbx3.set("")
    oprlog_cmbx["state"]=tk.DISABLED
    oprlog_cmbx3["state"]=tk.DISABLED

#CARGAR ARCHIVO -------------------------------------------------------------------------------------------
load = ttk.Frame(tabs)
#elementos
ca_lbl = ttk.Label(load, text="Archivo Cargado:",width=16) #Crea un label
ca_txt = ttk.Entry(load,width=50)
ca_txt.insert(0, "No hay ningun archivo cargado...")
def clearPanels():
    ruta = getSource()
    img3 = tk.PhotoImage(file= ruta+"\\src\\default\\default1.png")
    img4 = tk.PhotoImage(file= ruta+"\\src\\default\\default2.png")
    global panel1, panel2
    panel1.configure(image=img3)
    panel2.configure(image=img4)
    panel1.image=img3
    panel2.image=img4

def actualizaListas():
    opr_cmbx2["values"]=manejador.getLista().getNombres()
    opredit_cmbx["values"]=manejador.getLista().getNombres()
    oprlog_cmbx2["values"]=manejador.getLista().getNombres()
    opr_cmbx.set("")
    opr_cmbx2.set("")
    opredit_cmbx.set("")
    oprlog_cmbx2.set("")
    #LimpiezaPestañas
    defaultOpEd1()
    defaultOpEd2()
    defaultOpEd()

def cargarArchivo():
    file = filedialog.askopenfilename(title="Selecciona un archivo", filetypes=[("xml files", "*.xml")])
    if file:
        ca_txt.delete(0, tk.END)
        ca_txt.insert(0, str(file))
        manejador.cargarArchivo(file)
        actualizaListas()
        opLogicClear()
        clearPanels()
        # opr_cmbx2.values=manejador.getLista().getNombres()
        # print("archivo", file)

ca_btn = ttk.Button(load, text = "Abrir Archivo", width=13, command=cargarArchivo)

#INFO ----------------------------------------------------------------------------------------------------
info = ttk.Frame(tabs)
#elementos

info_btn1 = ttk.Button(info, text="Información del Estudiante")

def docum():
    manejador.openDocs(getSource())

info_btn2 = ttk.Button(info, text="Abrir Documentación", command=docum)

def muestraLogs():
    for logs in manejador.logsReport:
        print(logs)

info_btn3 = ttk.Button(info, text="Reporte HTML", command=muestraLogs)

#Creando las pestañas ------------------------------------------------------------------------------------
tabs.add(load, text="Cargar Archivo", padding=10)
tabs.add(oprtsn, text="Operaciones Básicas", padding=10)
tabs.add(opredit, text="Operaciones de Edición", padding=10)
tabs.add(oprlog, text="Operaciones Lógicas", padding=10)
tabs.add(info, text="Información", padding=10)

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
opredit_lbl.pack(side = tk.LEFT, padx=5, pady=5)
opredit_cmbx.pack(side = tk.LEFT, padx=5, pady=5)
opredit_lbl2.pack(side = tk.LEFT, padx=5, pady=5)
opredit_cmbx2.pack(side = tk.LEFT, padx=5, pady=5)
opredit_lbl3.pack(side = tk.LEFT, padx=5, pady=5)
opredit_cmbx3.pack(side = tk.LEFT, padx=5, pady=5)
opredit_lbl4.pack(side = tk.LEFT, padx=5, pady=5)
opredit_cmbx4.pack(side = tk.LEFT, padx=5, pady=5)
opredit_lbl5.pack(side = tk.LEFT, padx=5, pady=5)
opredit_cmbx5.pack(side = tk.LEFT, padx=5, pady=5)
opredit_lbl6.pack(side = tk.LEFT, padx=5, pady=5)
opredit_cmbx6.pack(side = tk.LEFT, padx=5, pady=5)
opredit_btn.pack(side = tk.LEFT, padx=5, pady=5)
opredit_btn2.pack(side = tk.LEFT, padx=5, pady=5)
oprlog_lbl2.pack(side = tk.LEFT, padx=5, pady=5)
oprlog_cmbx2.pack(side = tk.LEFT, padx=5, pady=5)
oprlog_lbl.pack(side = tk.LEFT, padx=5, pady=5)
oprlog_cmbx.pack(side = tk.LEFT, padx=5, pady=5)
oprlog_lbl3.pack(side = tk.LEFT, padx=5, pady=5)
oprlog_cmbx3.pack(side = tk.LEFT, padx=5, pady=5)
oprlog_btn.pack(side = tk.LEFT, padx=5, pady=5)
oprlog_btn2.pack(side = tk.LEFT, padx=5, pady=5)
info_btn1.pack(side = tk.LEFT, padx=5, pady=5)
info_btn2.pack(side = tk.LEFT, padx=5, pady=5)
info_btn3.pack(side = tk.LEFT, padx=5, pady=5)

tabs.pack(fill=tk.X)

panel1.pack(side = tk.TOP)
info1.pack(side = tk.BOTTOM, fill = tk.BOTH, expand=True)
panel2.pack(side = tk.TOP)
info2.pack(side = tk.BOTTOM, fill = tk.BOTH, expand=True)

pan_vista1.pack(side = tk.LEFT)
pan_vista2.pack(side = tk.RIGHT)

ventana.mainloop()

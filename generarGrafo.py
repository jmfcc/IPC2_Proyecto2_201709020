from os import system
from os import path
import time

def getsource():
    ruta = path.dirname(path.abspath(__file__)) #Obtiene la ruta del script en ejecución
    #print("lo que obtengo ",ruta)
    return ruta

def generagraf(nombre):
    di = "dot -Tpng " +  nombre + ".dot -o " + nombre + "-grafo.png"
    #print(di)
    mimetodo(di)
    # openGraf(nombre)
    
def escrituranorm(log, nombre):
    file = open(nombre + ".dot", "a")
    file. write(log + "\n")
    file. close()

def mimetodo(di):
    try:
        time.sleep(1)
        system (di)
        print(" >>> Grafo generado exitosamente...")
    except:
        print("Error al generar png")
    
def grafo(nombreM, filas, columnas, matriz, tipo):
    ruta = getsource()
    nombre = ruta + "\\img_" + tipo
    file = open(nombre + ".dot", "w")
    file.close()
    
    escrituranorm("digraph struct{", nombre)
    escrituranorm("\tgraph [dpi = 300];", nombre)
    escrituranorm("\tnode [shape = plaintext];", nombre)
        
    #CREACION DE NODOS
    log = "\tstruct [label=<"
    escrituranorm(log, nombre)
    log = "\t\t<TABLE BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\">"
    escrituranorm(log, nombre)
    #shape=doublecircle
    log = "\t\t\t<TR>"
    escrituranorm(log, nombre)

    #FILA CABECERA
    log = "\t\t\t\t<TD>" + nombreM + "</TD>"
    escrituranorm(log, nombre)
    for c in range(columnas):
        log = "\t\t\t\t<TD> " + str(c+1) + " </TD>"
        escrituranorm(log, nombre)
    log = "\t\t\t</TR>"
    escrituranorm(log, nombre)
    #FILAS DE MATRIZ E INDICES IZQUIERDOS
    aux = matriz.getInicio()
    contF = 1
    init = True
    while True:
        if init:
            log = "\t\t\t<TR>"
            escrituranorm(log, nombre)
            log = "\t\t\t\t<TD>" + str(contF) + "</TD>"
            escrituranorm(log, nombre)
            init = False
        if aux.getCaracter() == "*":
            log = "\t\t\t\t<TD> " + aux.getCaracter() + " </TD>"
        else:
            log = "\t\t\t\t<TD>   </TD>"
        escrituranorm(log, nombre)
        
        if aux.getSiguiente() != None:
            aux = aux.getSiguiente()
        else:
            log = "\t\t\t</TR>"
            escrituranorm(log, nombre)
            init = True
            contF += 1
            if aux.getInferior() != None:
                while aux.getAnterior() != None:
                    aux = aux.getAnterior()
                aux = aux.getInferior()
            else:
                break

    log = "\t\t</TABLE>>];"
    escrituranorm(log, nombre)
    log = "}"
    escrituranorm(log, nombre)
    
    generagraf(nombre)
    

# def openGraf(name):
#     di = "start " + name + "-grafo.png"
#     try:
#         time.sleep(2)
#         system (di)
#     except:
#         print("Error al abrir grafo")

from os import path
from ClaseLista import ListaImagenes, NodoImagen, imagen
from generarGrafo import grafo
from LectorXML import leerxml
from datetime import date
from datetime import datetime
from os import system
from time import sleep

biblioteca = ListaImagenes()
logsReport = []

def getLista():
    global biblioteca
    return biblioteca

def agregaImagen(nombre, filas, columnas, imagen):
    #new = NodoImagen(nombre, filas, columnas, imagen)
    global biblioteca
    biblioteca.agregaImagen(nombre, filas, columnas, imagen)

def agregaImagenOpLog(nombre, filas, columnas, imagen):
    #new = NodoImagen(nombre, filas, columnas, imagen)
    global biblioteca
    cVacios = (filas * columnas) - imagen.cuentaLlenos()
    if biblioteca.existeNombre(nombre):
        biblioteca.getNodeByName(nombre).setImagen(imagen)
        log = "Modificando matriz: " + nombre + " - Espacios llenos: " + str(imagen.cuentaLlenos()) + " - Espacios vacíos: " + str(cVacios)
        agregaLog(log)
    else:
        biblioteca.agregaImagen(nombre, filas, columnas, imagen)
        log = "Almacenando matriz: " + nombre + " - Espacios llenos: " + str(imagen.cuentaLlenos()) + " - Espacios vacíos: " + str(cVacios)
        agregaLog(log)

def agregaLog(log):
    fechaYhora = datetime.now().strftime('%d-%m-%Y - %H:%M:%S')
    logsReport.append(fechaYhora+" - "+log)

def union(nombre1, nombre2):   # <<<<<<<<<<<<<<<<
    global biblioteca
    img1 = biblioteca.getNodeByName(nombre1)
    img2 = biblioteca.getNodeByName(nombre2)
    if img1.getFilas() == img2.getFilas() and img1.getColumnas() == img2.getColumnas():
        log = "Operación: Unión - Matrices: " + nombre1 + " y " + nombre2
        agregaLog(log)
        aux1 = img1.getImagen().getInicio()
        aux2 = img2.getImagen().getInicio()
        newImg = imagen()
        nuevaFila = False
        while True:
            if aux1.getCaracter() == "*" or aux2.getCaracter() == "*":
                newImg.agregaNodo("*",nuevaFila)
            else:
                newImg.agregaNodo("-",nuevaFila)
            nuevaFila = False
            if aux1.getSiguiente() != None:
                aux1 = aux1.getSiguiente()
                aux2 = aux2.getSiguiente()
            else:
                nuevaFila = True
                if aux1.getInferior() != None:
                    while aux1.getAnterior() != None:
                        aux1 = aux1.getAnterior()
                        aux2 = aux2.getAnterior()
                    aux1 = aux1.getInferior()
                    aux2 = aux2.getInferior()
                else:
                    break
        imgTemporal = NodoImagen(img1.getNombre()+"-"+img2.getNombre(), img1.getFilas(), img1.getColumnas(), newImg)
        #newImg.muestraLista()
        generaImagenLogic(imgTemporal)
        return imgTemporal
    else:
        pass

def interseccion(nombre1, nombre2):   # <<<<<<<<<<<<<<<<
    global biblioteca
    img1 = biblioteca.getNodeByName(nombre1)
    img2 = biblioteca.getNodeByName(nombre2)
    if img1.getFilas() == img2.getFilas() and img1.getColumnas() == img2.getColumnas():
        log = "Operación: Intersección - Matrices: " + nombre1 + " y " + nombre2
        agregaLog(log)
        aux1 = img1.getImagen().getInicio()
        aux2 = img2.getImagen().getInicio()
        newImg = imagen()
        nuevaFila = False
        while True:
            if aux1.getCaracter() == "*" and aux2.getCaracter() == "*":
                newImg.agregaNodo("*",nuevaFila)
            else:
                newImg.agregaNodo("-",nuevaFila)
            nuevaFila = False
            if aux1.getSiguiente() != None:
                aux1 = aux1.getSiguiente()
                aux2 = aux2.getSiguiente()
            else:
                nuevaFila = True
                if aux1.getInferior() != None:
                    while aux1.getAnterior() != None:
                        aux1 = aux1.getAnterior()
                        aux2 = aux2.getAnterior()
                    aux1 = aux1.getInferior()
                    aux2 = aux2.getInferior()
                else:
                    break
        imgTemporal = NodoImagen(img1.getNombre()+"-"+img2.getNombre(), img1.getFilas(), img1.getColumnas(), newImg)
        #newImg.muestraLista()
        generaImagenLogic(imgTemporal)
        return imgTemporal
    else:
        pass

def diferencia(nombre1, nombre2):   # <<<<<<<<<<<<<<<<
    global biblioteca
    img1 = biblioteca.getNodeByName(nombre1)
    img2 = biblioteca.getNodeByName(nombre2)
    if img1.getFilas() == img2.getFilas() and img1.getColumnas() == img2.getColumnas():
        log = "Operación: Diferencia - Matrices: " + nombre1 + " y " + nombre2
        agregaLog(log)
        aux1 = img1.getImagen().getInicio()
        aux2 = img2.getImagen().getInicio()
        newImg = imagen()
        nuevaFila = False
        while True:
            if aux1.getCaracter() == "*" and aux2.getCaracter() != "*":
                newImg.agregaNodo("*",nuevaFila)
            else:
                newImg.agregaNodo("-",nuevaFila)
            nuevaFila = False
            if aux1.getSiguiente() != None:
                aux1 = aux1.getSiguiente()
                aux2 = aux2.getSiguiente()
            else:
                nuevaFila = True
                if aux1.getInferior() != None:
                    while aux1.getAnterior() != None:
                        aux1 = aux1.getAnterior()
                        aux2 = aux2.getAnterior()
                    aux1 = aux1.getInferior()
                    aux2 = aux2.getInferior()
                else:
                    break
        imgTemporal = NodoImagen(img1.getNombre()+"-"+img2.getNombre(), img1.getFilas(), img1.getColumnas(), newImg)
        #newImg.muestraLista()
        generaImagenLogic(imgTemporal)
        return imgTemporal
    else:
        pass

def diferenciaSimetrica(nombre1, nombre2):   # <<<<<<<<<<<<<<<<
    global biblioteca
    img1 = biblioteca.getNodeByName(nombre1)
    img2 = biblioteca.getNodeByName(nombre2)
    if img1.getFilas() == img2.getFilas() and img1.getColumnas() == img2.getColumnas():
        log = "Operación: Diferencia Simétrica - Matrices: " + nombre1 + " y " + nombre2
        agregaLog(log)
        aux1 = img1.getImagen().getInicio()
        aux2 = img2.getImagen().getInicio()
        newImg = imagen()
        nuevaFila = False
        while True:
            if aux1.getCaracter() == "*" and aux2.getCaracter() != "*":
                newImg.agregaNodo("*",nuevaFila)
            elif aux2.getCaracter() == "*" and aux1.getCaracter() != "*":
                newImg.agregaNodo("*",nuevaFila)
            else:
                newImg.agregaNodo("-",nuevaFila)
            nuevaFila = False
            if aux1.getSiguiente() != None:
                aux1 = aux1.getSiguiente()
                aux2 = aux2.getSiguiente()
            else:
                nuevaFila = True
                if aux1.getInferior() != None:
                    while aux1.getAnterior() != None:
                        aux1 = aux1.getAnterior()
                        aux2 = aux2.getAnterior()
                    aux1 = aux1.getInferior()
                    aux2 = aux2.getInferior()
                else:
                    break
        imgTemporal = NodoImagen(img1.getNombre()+"-"+img2.getNombre(), img1.getFilas(), img1.getColumnas(), newImg)
        #newImg.muestraLista()
        generaImagenLogic(imgTemporal)
        return imgTemporal
    else:
        pass

def operationEdit(nombre, tipo, params):   # <<<<<<<<<<<<<<<<
    global biblioteca
    nodoMatriz = biblioteca.getNodeByName(nombre)
    log = ""
    if tipo == "Limpiar área":
        log = "Operación: " + tipo + " - Matriz: " + nombre
    else:
        log = "Operación: Agregar " + tipo + " - Matriz: " + nombre
    if tipo == "Limpiar área":
        nodoMatriz.getImagen().limpiaArea(params[0], params[1], params[2], params[3])
    elif tipo == "Linea Horiz.":
        nodoMatriz.getImagen().lineaHoriz(params[0], params[1], params[2])
    elif tipo == "Linea Vert.":
        nodoMatriz.getImagen().lineaVerti(params[0], params[1], params[2])
    elif tipo == "Rectángulo":
        nodoMatriz.getImagen().rectangulo(params[0], params[1], params[2], params[3])
    elif tipo == "Triángulo":
        nodoMatriz.getImagen().triangulo(params[0], params[1], params[2])
    agregaLog(log)
    grafo(nodoMatriz.getNombre(), nodoMatriz.getFilas(), nodoMatriz.getColumnas(), nodoMatriz.getImagen(), "modificada")

def tamanioImagen(nombre):
    nodoMatriz = biblioteca.getNodeByName(nombre)
    dimensiones = [nodoMatriz.getFilas(), nodoMatriz.getColumnas()]
    return dimensiones

def cargarArchivo(ruta):
    global biblioteca
    if biblioteca:
        biblioteca = None
        biblioteca = ListaImagenes()
    #Abrir un archvo
    ph, fh = path.split(ruta)
    nombre, extension = path.splitext(fh)
    if extension == ".xml":
        try:
            log = "Cargando archivo: " + nombre + extension
            agregaLog(log)
            leerxml(ruta, nombre+extension)
            log = "Carga de archivo: " + nombre + extension + " completa"
            agregaLog(log)
            print(" >>> Lectura de archivo completa\n")
        except:
            log = "Carga de archivo: " + nombre + extension + " incompleta, se detectaron errores"
            agregaLog(log)
            print("\n >>> Error: La lectura no se completo correctamente, verifique su archivo de entrada\n")
    else:
        print(" >>> El archivo no es de extensión XML")
    
def generaImagenMod(seleccion, tipo, tipo_name):   # <<<<<<<<<<<<<<<<
    global biblioteca
    if seleccion:
        if biblioteca.existeNombre(seleccion):
            log = "Operación: " + tipo_name + " - Matriz: " + seleccion
            agregaLog(log)
            biblioteca.setImgNodeByName(seleccion, tipo)
            nodoMatriz = biblioteca.getNodeByName(seleccion)
            grafo(nodoMatriz.getNombre(), nodoMatriz.getFilas(), nodoMatriz.getColumnas(), nodoMatriz.getImagen(), "modificada")
        else:
            log = "Error de operación " + tipo_name + " - Matriz inexistente: " + seleccion
            agregaLog(log)
            print(" >>> Selección inválida")
    else:
        log = "Error de operación " + tipo_name + " - Matriz: sin seleccionar"
        agregaLog(log)
        print(" >>> Aviso: Debes elegir una opción")
    
def generaImagenLogic(nodoMatriz):
    grafo(nodoMatriz.getNombre(), nodoMatriz.getFilas(), nodoMatriz.getColumnas(), nodoMatriz.getImagen(), "opLogic")

def generaImagenO(seleccion):
    global biblioteca
    if seleccion:
        if biblioteca.existeNombre(seleccion):
            nodoMatriz = biblioteca.getNodeByName(seleccion)
            grafo(nodoMatriz.getNombre(), nodoMatriz.getFilas(), nodoMatriz.getColumnas(), nodoMatriz.getImagen(), "original")
        else:
            print(" >>> Selección inválida")
    else:
        print(" >>> Aviso: Debes elegir una opción")

def generaImagenO2(seleccion):
    global biblioteca
    if seleccion:
        if biblioteca.existeNombre(seleccion):
            nodoMatriz = biblioteca.getNodeByName(seleccion)
            grafo(nodoMatriz.getNombre(), nodoMatriz.getFilas(), nodoMatriz.getColumnas(), nodoMatriz.getImagen(), "original2")
        else:
            print(" >>> Selección inválida")
    else:
        print(" >>> Aviso: Debes elegir una opción")

def openDocs(ruta):
    di = "start " + ruta + "\\docs\\Doc_P2_IPC2.pdf"
    try:
        sleep(0.6)
        system (di)
    except:
        print("Error al abrir documentación")
from os import path
from ClaseLista import ListaImagenes, NodoImagen
from generarGrafo import grafo
from LectorXML import leerxml

biblioteca = ListaImagenes()

def getLista():
    global biblioteca
    return biblioteca

def agregaImagen(nombre, filas, columnas, imagen):
    #new = NodoImagen(nombre, filas, columnas, imagen)
    global biblioteca
    biblioteca.agregaImagen(nombre, filas, columnas, imagen)

def listaImagenes():
    global biblioteca
    return biblioteca.getNombres()

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
            leerxml(ruta, nombre+extension)
            print(" >>> Lectura de archivo completa\n")
        except:
            print("\n >>> Error: La lectura no se completo correctamente, verifique su archivo de entrada\n")
    else:
        print(" >>> El archivo no es de extensión XML")
    
def generaImagen(seleccion, tipo):
    global biblioteca
    # biblioteca.muestraNombres()
    # seleccion = input(" >>> Ingresa el nombre de la matriz para generar su grafo: ")
    if seleccion:
        if biblioteca.existeNombre(seleccion):
            nodoMatriz = biblioteca.getNodeByName(seleccion)
            grafo(nodoMatriz.getNombre(), nodoMatriz.getFilas(), nodoMatriz.getColumnas(), nodoMatriz.getImagen(), "original")
            biblioteca.setImgNodeByName(seleccion, tipo)
            nodoMatriz = biblioteca.getNodeByName(seleccion)
            grafo(nodoMatriz.getNombre(), nodoMatriz.getFilas(), nodoMatriz.getColumnas(), nodoMatriz.getImagen(), "modificada")
            #print(nodoMatriz.getMatriz().dameMatrizEnFormato())
        else:
            print(" >>> Selección inválida")
    else:
        print(" >>> Aviso: Debes elegir una opción")

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
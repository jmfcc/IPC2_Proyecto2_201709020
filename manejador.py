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

def cargarArchivo():
    global biblioteca
    if biblioteca:
        biblioteca = None
        biblioteca = ListaImagenes()
    #Abrir un archvo
    try:
        leerxml("C:/Users/Jaime/Documents/DEVELOP/PYTHON/2021_1S/IPC2_Proyecto2_201709020/entrada.xml", "Entrada.xml")
    except:
        print(" >> Error: Fromato inválido")

def generaImagen():
    global biblioteca
    biblioteca.muestraNombres()
    seleccion = input(" >>> Ingresa el nombre de la matriz para generar su grafo: ")
    if seleccion:
        if biblioteca.existeNombre(seleccion):
            nodoMatriz = biblioteca.getNodeByName(seleccion)
            grafo(nodoMatriz.getNombre(), nodoMatriz.getFilas(), nodoMatriz.getColumnas(), nodoMatriz.getImagen(), "Original")
            #print(nodoMatriz.getMatriz().dameMatrizEnFormato())
        else:
            print(" >>> Selección inválida")
    else:
        print(" >>> Aviso: Debes elegir una opción")
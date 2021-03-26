from xml.dom import minidom
import time
from ClaseLista import imagen
import manejador


def leerxml(ruta, nArchivo): 
    print(" >>> Obteniendo archivo de ", ruta)
    time.sleep(0.6)
    archivo = minidom.parse(ruta)
    print(" >>> Lectura de "+ nArchivo +"\n")
    for matrix in archivo.getElementsByTagName("matrices"):
        for matriz in matrix.getElementsByTagName("matriz"):
            taBien = True
            nombre = matriz.getElementsByTagName("nombre")[0].firstChild.data
            # Validar nombre
            if validaNombre(nombre):
                print(" >>> Error: Se encontró una imagen existente con el nombre " + nombre)
                #break
            else:
                try:
                    filas = int(matriz.getElementsByTagName("filas")[0].firstChild.data)
                    columnas = int(matriz.getElementsByTagName("columnas")[0].firstChild.data)
                    img = matriz.getElementsByTagName("imagen")[0].firstChild.data
                    img = img.replace(" ","")
                    #print("Nombre:",nombre, " Filas:", filas, " Cols:", columnas)
                    cont = 0
                    contF = 0
                    for char in img:
                        if char == "\n":
                            if cont == 0:
                                pass
                            elif cont != columnas:
                                taBien = False
                                if cont > columnas:
                                    print(" >>> Error: Indice de columna fuera de rango en la matriz", nombre)
                                else:
                                    print(" >>> Error: Valores de columna faltantes en la matriz", nombre)
                                break
                            else:
                                contF += 1
                                cont = 0
                                if contF > filas:
                                    print(" >>> Error: El número de filas es mayor al tamaño limite de la matriz", nombre)
                                    break
                        else:
                            if char == "-" or char == "*":
                                cont += 1
                            else:
                                print(" >>> Error: Se encontraron valores no válidos en la matriz", nombre)
                                taBien = False
                                break                    
                    if contF < filas and taBien:
                        print(" >>> Error: El número de filas es menor al tamaño limite de la matriz", nombre)
                        taBien = False
                    if taBien:
                        img_tmp = imagen()
                        cont = 0
                        esNueva = True
                        for char in img:
                            if char == "\n":
                                if cont == 0:
                                    pass
                                else:
                                    esNueva = True
                                    cont = 0
                                #print("Linea")
                            else:
                                if esNueva:
                                    cont += 1
                                    img_tmp.agregaNodo(char, esNueva)
                                    esNueva = False
                                else:
                                    cont += 1
                                    img_tmp.agregaNodo(char, esNueva)
                                cont += 1
                        manejador.agregaImagen(nombre, filas, columnas, img_tmp)
                        print(" >>> Imagen:", nombre, " almacenada correctamente")
                except:
                    print(" >>> Error: Se ha detectado un valor no numérico en el atributo tamaño")
    time.sleep(0.4)
    # return

def validaNombre(nombre):
    lista = manejador.getLista()
    if not lista.estaVacia():
        return lista.existeNombre(nombre)
    return False
   
#leerxml("C:/Users/Jaime/Documents/DEVELOP/PYTHON/2021_1S/IPC2_Proyecto2_201709020/entrada.xml", "Entrada.xml")
# leerxml()

# img_tmp.muestraLista()
# grafo(nombre, filas, columnas, img_tmp, "Original")
# print("Imagen con rotación Horizontal:")
# img_tmp.rotaImagen("h")
# img_tmp.muestraLista()
# grafo(nombre, filas, columnas, img_tmp, "Modif")
# print("Imagen con rotación Vertical:")
# img_tmp.rotaImagen("h")
# img_tmp.rotaImagen("v")
# img_tmp.muestraLista()
# print("Imagen transpuesta:")
# img_tmp.rotaImagen("t")
# img_tmp.muestraLista()
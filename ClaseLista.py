class NodoMultidireccional():

    def __init__(self, caracter):
        self.caracter = caracter
        self.superior = None
        self.inferior = None
        self.anterior = None
        self.siguiente = None

    def getCaracter(self):
        return self.caracter
    def getSuperior(self):
        return self.superior
    def getInferior(self):
        return self.inferior
    def getAnterior(self):
        return self.anterior
    def getSiguiente(self):
        return self.siguiente

    def setCaracter(self, caracter):
        self.caracter = caracter
    def setSuperior(self, nodo):
        self.superior = nodo
    def setInferior(self, nodo):
        self.inferior = nodo
    def setAnterior(self, nodo):
        self.anterior = nodo
    def setSiguiente(self, nodo):
        self.siguiente = nodo

    def reflejaHorizontal(self):
        apuntadorTemporal = self.superior
        self.superior = self.inferior
        self.inferior = apuntadorTemporal
    
    def reflejaVertical(self):
        apuntadorTemporal = self.anterior
        self.anterior = self.siguiente
        self.siguiente = apuntadorTemporal

    def rotaIzq(self):
        apuntadorTemporal = self.superior
        self.superior = self.siguiente
        self.siguiente = self.inferior
        self.inferior = self.anterior
        self.anterior = apuntadorTemporal


class imagen(): #Lista Ortogonal

    def __init__(self):
        self.inicio = None

    def getInicio(self):
        return self.inicio

    def estaVacia(self):
        return self.inicio == None

    def agregaNodo(self, caracter, nuevaFila):
        if self.estaVacia():
            temporal = NodoMultidireccional(caracter)
            self.inicio = temporal
        else:
            conectorV = self.inicio
            while conectorV.getInferior() != None:
                conectorV = conectorV.getInferior()

            tmp = NodoMultidireccional(caracter)
            if nuevaFila:
                conectorV.setInferior(tmp)
                tmp.setSuperior(conectorV)
            else:
                conectorH = conectorV.getSuperior()
                while conectorV.getSiguiente() != None:
                    if conectorH != None:
                        conectorH = conectorH.getSiguiente()
                    conectorV = conectorV.getSiguiente()

                conectorV.setSiguiente(tmp)
                tmp.setAnterior(conectorV)
                
                if conectorH != None:
                    conectorH = conectorH.getSiguiente()
                    conectorH.setInferior(tmp)
                    tmp.setSuperior(conectorH)

    def muestraLista(self):
        aux = self.inicio
        concat = ""
        while True:
            concat += aux.getCaracter()
            if aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            else:
                print(concat)
                concat = ""
                if aux.getInferior() != None:
                    while aux.getAnterior() != None:
                        aux = aux.getAnterior()
                    aux = aux.getInferior()
                else:
                    break
    
    def rotaImagen(self, tipo):
        if tipo == "h":
            aux = self.inicio
            while True:
                aux.reflejaHorizontal()
                if aux.getSiguiente() != None:
                    aux = aux.getSiguiente()
                else:
                    if aux.getSuperior() != None:
                        while aux.getAnterior() != None:
                            aux = aux.getAnterior()
                        aux = aux.getSuperior()
                    else:
                        break
            while self.inicio.getSuperior() != None:
                self.inicio = self.inicio.getSuperior()
        elif tipo == "v":
            aux = self.inicio
            while True:
                aux.reflejaVertical()
                if aux.getInferior() != None:
                    aux = aux.getInferior()
                else:
                    if aux.getAnterior() != None:
                        while aux.getSuperior() != None:
                            aux = aux.getSuperior()
                        aux = aux.getAnterior()
                    else:
                        break
            while self.inicio.getAnterior() != None:
                self.inicio = self.inicio.getAnterior()
        elif tipo == "t":
            aux = self.inicio
            while True:
                aux.rotaIzq()
                if aux.getSuperior() != None:
                    aux = aux.getSuperior()
                else:
                    if aux.getSiguiente() != None:
                        while aux.getInferior() != None:
                            aux = aux.getInferior()
                        aux = aux.getSiguiente()
                    else:
                        break
            while self.inicio.getSuperior() != None:
                self.inicio = self.inicio.getSuperior()


class NodoImagen():

    def __init__(self, nombre, filas, columnas, img):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.img = img
        self.siguiente = None
    
    def getNombre(self):
        return self.nombre
    def getFilas(self):
        return self.filas
    def getColumnas(self):
        return self.columnas
    def getImagen(self):
        return self.img
    def getSiguiente(self):
        return self.siguiente

    def setNombre(self, nombre):
        self.nombre = nombre
    def setFilas(self, filas):
        self.filas = filas
    def setColumnas(self, columnas):
        self.columnas = columnas
    def setImagen(self, img):
        self.img = img
    def setSiguiente(self, siguiente):
        self.siguiente = siguiente
    
class ListaImagenes():

    def __init__(self):
        self.inicio = None
    
    def estaVacia(self):
        return self.inicio == None

    def getInicio(self):
        return self.inicio

    def agregaImagen(self, nombre, filas, columnas, img):
        if self.estaVacia():
            tmp = NodoImagen(nombre, filas, columnas, img)
            self.inicio = tmp
        else:
            aux = self.inicio
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            
            tmp = NodoImagen(nombre, filas, columnas, img)
            aux.setSiguiente(tmp)
    
    def muestraNombres(self):
        aux = self.inicio
        while True:
            print(" >>", aux.getNombre())
            if aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            else:
                break

    def existeNombre(self, nombre):
        aux = self.inicio
        while True:
            if aux.getNombre() == nombre:
                return True
            if aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            else:
                break
        return False

    def getNodeByName(self, nombre):
        aux = self.inicio
        while True:
            if aux.getNombre() == nombre:
                return aux
            if aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            else:
                break
    
    def setImgNodeByName(self, nombre, pos):
        aux = self.inicio
        while True:
            if aux.getNombre() == nombre:
                if pos == "h" or pos == "v":
                    aux.getImagen().rotaImagen(pos)
                else:
                    aux.getImagen().rotaImagen("v")
                    aux.getImagen().rotaImagen(pos)
            if aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            else:
                break
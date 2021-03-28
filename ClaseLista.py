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

    def limpiaArea(self, f_ini, f_fin, c_ini, c_fin):
        aux = self.inicio
        contF = 1
        contC = 1
        #Ubicarse en las posiciones iniciales
        while contF < f_ini:
            aux = aux.getInferior()
            contF += 1
        while contC < c_ini:
            aux = aux.getSiguiente()
            contC += 1
        #Limpiar area
        while True:
            if contF == f_fin and contC == c_fin:
                aux.setCaracter("-")
                break
            else:
                while contC < c_fin:
                    aux.setCaracter("-")
                    aux = aux.getSiguiente()
                    contC += 1
                aux.setCaracter("-")
                if contF < f_fin:
                    while contC > c_ini:
                        aux = aux.getAnterior()
                        contC -= 1
                    aux = aux.getInferior()
                    contF += 1
                else:
                    break

    def lineaHoriz(self, fil, c_ini, c_fin):
        aux = self.inicio
        contF = 1
        contC = 1
        #Ubicarse en las posiciones iniciales
        while contF < fil:
            aux = aux.getInferior()
            contF += 1
        while contC < c_ini:
            aux = aux.getSiguiente()
            contC += 1
        #Recorrer columnas
        while contC < c_fin:
            aux.setCaracter("*")
            aux = aux.getSiguiente()
            contC += 1
        aux.setCaracter("*")

    def lineaVerti(self, f_ini, f_fin, col):
        aux = self.inicio
        contF = 1
        contC = 1
        #Ubicarse en las posiciones iniciales
        while contF < f_ini:
            aux = aux.getInferior()
            contF += 1
        while contC < col:
            aux = aux.getSiguiente()
            contC += 1
        #Recorrer filas
        while contF < f_fin:
            aux.setCaracter("*")
            aux = aux.getInferior()
            contF += 1
        aux.setCaracter("*")

    def rectangulo(self, f_ini, altr, c_ini, anch):
        aux = self.inicio
        contF = 1
        contC = 1
        #Ubicarse en las posiciones iniciales
        while contF < f_ini:
            aux = aux.getInferior()
            contF += 1
        while contC < c_ini:
            aux = aux.getSiguiente()
            contC += 1
        #Recorrer derecha
        while contC < c_ini+anch-1:
            aux.setCaracter("*")
            aux = aux.getSiguiente()
            contC += 1
        #Recorrer abajo
        while contF < f_ini+altr-1:
            aux.setCaracter("*")
            aux = aux.getInferior()
            contF += 1
        #Recorrer atras
        while contC > c_ini:
            aux.setCaracter("*")
            aux = aux.getAnterior()
            contC -= 1
        #Recorrer arriba
        while contF > f_ini:
            aux.setCaracter("*")
            aux = aux.getSuperior()
            contF -= 1
        aux.setCaracter("*")

    def triangulo(self, fil, col, tam):
        aux = self.inicio
        contF = 1
        contC = 1
        #Ubicarse en las posiciones iniciales
        while contF < fil:
            aux = aux.getInferior()
            contF += 1
        while contC < col:
            aux = aux.getSiguiente()
            contC += 1
        #Recorrer filas
        while contF < fil+tam-1:
            aux.setCaracter("*")
            aux = aux.getInferior()
            contF += 1
        #Recorrer coulumnas
        while contC < col+tam-1:
            aux.setCaracter("*")
            aux = aux.getSiguiente()
            contC += 1
        aux.setCaracter("*")
        #Recorrer en escalera
        if tam > 2:
            repeat = tam - 2
            contRep = 1
            while contRep <= repeat:
                aux = aux.getAnterior().getSuperior()
                aux.setCaracter("*")
                contRep += 1 


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
    
    def redimensionaImg(self):
        tmp = self.filas
        self.filas = self.columnas
        self.columnas = tmp

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
    
    def getNombres(self):
        elem_comboBox = []
        if self.estaVacia():
            return elem_comboBox
        else:
            aux = self.inicio
            while True:
                elem_comboBox.append(aux.getNombre())
                if aux.getSiguiente() != None:
                    aux = aux.getSiguiente()
                else:
                    break
            return elem_comboBox

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
    
    def filtroDimensiones(self, nombre):
        elem_comboBox = []
        if self.estaVacia():
            return elem_comboBox
        else:
            aux = self.inicio
            img = self.getNodeByName(nombre)
            while True:
                if img.getFilas() == aux.getFilas() and img.getColumnas() == aux.getColumnas():
                    elem_comboBox.append(aux.getNombre())
                if aux.getSiguiente() != None:
                    aux = aux.getSiguiente()
                else:
                    break
            return elem_comboBox

    def setImgNodeByName(self, nombre, pos):
        aux = self.inicio
        while True:
            if aux.getNombre() == nombre:
                if pos == "h" or pos == "v":
                    aux.getImagen().rotaImagen(pos)
                else:
                    aux.getImagen().rotaImagen("v")
                    aux.getImagen().rotaImagen(pos)
                    aux.redimensionaImg()
            if aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            else:
                break
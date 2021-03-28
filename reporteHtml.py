from os import path
from os import system
from time import sleep

def getSource():
    ruta = path.dirname(path.abspath(__file__)) #Obtiene la ruta del script en ejecución
    return ruta

def escrituranorm(log, nombre):
    file = open(nombre, "a", encoding='utf-8')
    file. write(log + "\n")
    file. close()

def reportar(listaLogs):
    nombre = getSource() + "\\src\\reports\\reportLog.html"
    file = open(nombre, "w")
    file.close()

    escrituranorm("<!DOCTYPE html>\n"
    +"<html lang=\"en\">\n"
    +"<head>\n"
    +"    <meta charset=\"UTF-8\">\n"
    +"    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n"
    +"    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
    +"    <title>Document</title>\n"
    +"    <link rel=\"stylesheet\" href=\"https://bootswatch.com/4/lux/bootstrap.css\">\n"
    +"    <link rel=\"stylesheet\" href=\"https://bootswatch.com/_assets/css/custom.min.css\">\n"
    +"</head>\n"
    +"<body>\n"
    +"    <div class=\"container\">\n"
    +"        <h1>LOGS</h1>\n"
    +"        <table class=\"table table-hover\">\n"
    +"            <tbody>\n", nombre)
    liLog = listaLogs.copy()
    liLog.reverse()
    alternar = False
    for log in liLog:
        logData = ""
        if alternar:
            logData = "\t\t\t<tr class=\"table-primary\">\n"
            alternar = False
        else:
            logData = "\t\t\t<tr class=\"table-secondary\">\n"
            alternar = True
        escrituranorm(logData
        +"\t\t\t\t<th scope=\"row\">"+log+"</th>\n"
        +"\t\t\t</tr>\n", nombre)

    escrituranorm("            </tbody>\n"
        +"        </table>\n"
        +"    </div>\n"
        +"</body>\n"
        +"</html>", nombre)

    openReport(nombre)

def openReport(archivo):
    di = "start " + archivo
    try:
        sleep(0.6)
        system (di)
    except:
        print("Error al abrir reporte")


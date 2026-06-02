from easygui import *
import easygui

def ini_int():
    #Variables encargadas de dar los mensajes y guardar valores:
    mensaje_inicial = "¡Hola Usuario! Bienvenido al programa del Juego de la Vida de Conway y La Hormiga de Langton."
    decision = "¿Desea usted continuar?"
    mensaje_despedida = "¡Hasta pronto, tenga bonito día!"
    decisiones = ["CONWAY","LANGTON"]
    titulo = "PROGRAMA PRINCIPAL"
    reglas = 0
    filas = 0
    cols = 0
    celdas = 0
    mensaje_pedida = "Introduzca las reglas,filas,columnas y el tamaño:"
    titulo_pedida = "DATOS NECESARIOS"
    nombres_de_datos = ["Reglas","Filas","Columnas","Tamaño de celdas"]
    valor_de_datos = []

    #Interfaz principal:

    if ccbox(mensaje_inicial,choices=("CONTINUAR", "SALIR")) == True:   
        programas =buttonbox("Escoja que desea hacer:",titulo,decisiones)
        if programas == "CONWAY":
            msgbox("Escogiste Conway")
            valor_de_datos = multenterbox(mensaje_pedida,titulo_pedida, nombres_de_datos)
            if valor_de_datos == None:
                msgbox(mensaje_despedida)
            elif valor_de_datos[0] == "":
                msgbox("La lista está vacia, por favor introduzca los datos")
        elif programas == "LANGTON":
            msgbox("Escogiste Langton")
            valor_de_datos = multenterbox(mensaje_pedida,titulo_pedida, nombres_de_datos)
            if valor_de_datos == None:
                msgbox(mensaje_despedida)
            elif valor_de_datos[0] == "":
                msgbox("La lista está vacia, por favor introduzca los datos")
        else:
            msgbox(mensaje_despedida)
    else:
        msgbox(mensaje_despedida)

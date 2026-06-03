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
    i = 0

    #Interfaz principal:

    if ccbox(mensaje_inicial,choices=("CONTINUAR", "SALIR")) == True:   
        programas =buttonbox("Escoja que desea hacer:",titulo,decisiones)
        if programas == "CONWAY":
            msgbox("Escogiste Conway")
            valor_de_datos = multenterbox(mensaje_pedida,titulo_pedida, nombres_de_datos)
            print(valor_de_datos)
            if valor_de_datos == None:
                msgbox(mensaje_despedida)
            while i != len(valor_de_datos):
                if valor_de_datos[i] == "":
                    msgbox("La lista está vacia, por favor introduzca los datos")
                    raise Exception("No se puede enviar a la funcion esta lista")
                else:
                    i +=1   
            pre_ini_int(valor_de_datos,programas)
        elif programas == "LANGTON":
            msgbox("Escogiste Langton")
            valor_de_datos = multenterbox(mensaje_pedida,titulo_pedida, nombres_de_datos)
            if valor_de_datos == None:
                msgbox(mensaje_despedida)
            while i != len(valor_de_datos):
                if valor_de_datos[i] == "":
                    msgbox("La lista está vacia, por favor introduzca los datos")
                    i = len(valor_de_datos)
                    raise Exception("No se puede enviar a la funcion esta lista")
                else:
                    i +=1
            pre_ini_int(valor_de_datos,programas)
        else:
            msgbox(mensaje_despedida)
    else:
        msgbox(mensaje_despedida)
    
def pre_ini_int(L, programas):
    #Funcion que prepara los strings para llevarlos a cada función
    reglas = L[0]
    filas = int(L[1])
    columnas = int(L[2])
    tamaño = int(L[3])

    #for editar todo
    if programas == "CONWAY":
        birth = list(reglas[0:reglas.index("/")])
        surv = list(reglas[reglas.index("/"):])
        print(birth,surv)
        if any(birth) == int:
            pass
        else:
            raise Exception("Necesita por lo menos un numero")
        if any(surv) == int:
            pass
        else:
            raise Exception("Necesita por lo menos un numero")
        
    else:
        pass
    
    

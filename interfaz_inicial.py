from easygui import *
import langton_ant_gui as horlan2
import life_like_gui as lili


def ini_int():
    """
    Interfaz principal del programa.
    Entradas y restricciones:
    - Ninguna.
    Salidas:
    - Ninguna (despliega ventanas emergentes y llama a otras funciones).
    Autores:
    Andrey Morales Reyes
    Alexei Quesada Leandro
    """
    #Variables encargadas de dar los mensajes y guardar valores:
    mensaje_inicial = "¡Hola Usuario! Bienvenido al programa del Juego de la Vida de Conway y La Hormiga de Langton."
    decision = "¿Desea usted continuar?"
    mensaje_despedida = "¡Hasta pronto, tenga bonito día!"
    decisiones = ["CONWAY","LANGTON"]
    titulo = "PROGRAMA PRINCIPAL"
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
                    ini_int()
                    return
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
                    ini_int()
                    return
                else:
                    i +=1
            pre_ini_int(valor_de_datos,programas)
        else:
            msgbox(mensaje_despedida)
    else:
        msgbox(mensaje_despedida)
    
def pre_ini_int(L, programas):
    """
    Función que prepara y valida los datos antes de iniciar la simulación.
    Entradas y restricciones:
    - L: Lista que contiene [Reglas, Filas, Columnas, Tamaño].
    - Filas, Columnas y Tamaño deben ser números enteros mayores a 0.
      Restricciones para CONWAY: Las filas y columnas deben ser iguales. Las reglas deben contener una "/" y al menos un número para nacimiento y otro para supervivencia.
      estricciones para LANGTON: Las reglas solo pueden contener las letras 'R' y 'L'.
    - programas: String con el nombre del juego ("CONWAY" o "LANGTON").
    Salidas:
    - Ninguna (transfiere el control a los módulos principales de cada juego).
    Autores:
    Andrey Morales Reyes
    Alexei Quesada Leandro
    """
    #Funcion que prepara los strings para llevarlos a cada función
    reglas = L[0]
    if L[1].isdigit() == False:
        msgbox("Introduzca números enteros en la cantidad de filas.")
        ini_int()
        return
    elif L[2].isdigit() == False:
        msgbox("Introduzca números enteros en la cantidad de columnas.")
        ini_int()
        return
    elif L[3].isdigit() == False:
        msgbox("Introduzca números enteros en el tamaño.")
        ini_int()
        return
    filas = int(L[1])
    if filas < 1:
        msgbox("Introduzca números enteros mayores a 0 en las filas.")
        ini_int()
        return
    columnas = int(L[2])
    if columnas < 1:
        msgbox("Introduzca números enteros mayores a 0 en las columnas.")
        ini_int()
        return
    tamaño = int(L[3])
    contador = 0
    #para editar todo
    if programas == "CONWAY":
        if L[0].find("/")== -1:
            msgbox("Introduzca una separación entre reglas válida, ejemplo B23/S234.")
            ini_int()
            return
        elif filas != columnas:
            msgbox("El tamaño de filas y columnas debe ser el mismo")
            ini_int()
        else:
         global birth, surv
         birth = list(reglas[0:reglas.index("/")])
         surv = list(reglas[reglas.index("/")+1:])
        for i in range(len(birth)):
            if birth[i].isdigit() == True:
                contador += 1
        if contador < 1:
            msgbox("Introduzca al menos un número entero en la regla de nacimiento.")
            ini_int()
            return
        contador = 0
        for i in range(len(surv)):
            if surv[i].isdigit() == True:
                contador += 1
        if contador < 1:
            msgbox("Introduzca al menos un número entero en la regla de sobrevivir.")
            ini_int()
            return
        lili.main(surv,birth,tamaño,filas,columnas)
        
    else:
        reglas = reglas.upper()
        for i in range(len(L[0])):
            if reglas[i] != "L" and reglas[i] != "R":
                msgbox("Introduzca una combinación de R Y L solamente.")
                ini_int()
                return        
        
        horlan2.main(reglas,filas,columnas,tamaño)
        
            

if __name__ == "__main__":
    ini_int()
    

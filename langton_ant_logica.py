#Creadores
#Andrey Morales Reyes
#Alexei Quesada Leandro

import random
import interfaz_inicial

matriz = []
revisor = []
célula = 0

ant_f = 0
ant_c = 0
hormiga = -1
dirección = "U"

colores = []
color = []
giro = []

def siguiente(giro, célula, matriz):
    """Función que determina la siguiente posición de la hormiga en la matriz.
    Entradas y restricciones:
    - giro: Lista formada del string de Ls y Rs: Sin restricciones.
    - célula: Valor de la posición actual en la matriz: Sin restricciones.
    - matriz: Matriz por la que se desplaza la hormiga: Sin restricciones.
    Salidas:
    - Siguiente posición de la hormiga.
    Autores:
    Andrey Morales Reyes
    Alexei Quesada Leandro"""
    if dirección == "R" and giro[célula % len(giro)] == "R" or dirección == "L" and giro[célula % len(giro)] == "L":
        girar_hormiga("D")
        return (ant_f + 1) % len(matriz), ant_c
    elif dirección == "R" and giro[célula % len(giro)] == "L" or dirección == "L" and giro[célula % len(giro)] == "R":
        girar_hormiga("U")
        return (ant_f - 1) % len(matriz), ant_c
    elif dirección == "U" and giro[célula % len(giro)] == "R" or dirección == "D" and giro[célula % len(giro)] == "L":
        girar_hormiga("R")
        return ant_f, (ant_c + 1) % len(matriz[0])
    elif dirección == "U" and giro[célula % len(giro)] == "L" or dirección == "D" and giro[célula % len(giro)] == "R":
        girar_hormiga("L")
        return ant_f, (ant_c - 1) % len(matriz[0])

def girar_hormiga(nueva_dirección):
    """Procedimiento que recibe una dirección y actualiza la orientación de la hormiga.
    Entradas y restricciones:
    - dirección: Dirección actual de la hormiga: Sin restricciones.
    - nueva_dirección: Dirección nueva de la hormiga: Sin restricciones.
    Salidas:
    - Nueva dirección de la hormiga.
    Autores:
    Andrey Morales Reyes
    Alexei Quesada Leandro"""
    global dirección
    if nueva_dirección in ("U", "D") and dirección in ("L", "R"):
        dirección = nueva_dirección
    elif nueva_dirección in ("L", "R") and dirección in ("U", "D"):
        dirección = nueva_dirección

def avanzar_hormiga():
    """Procedimiento que se encarga de hacer avanzar a la hormiga a la siguiente posición en la matriz.
    Entradas y restricciones:
    - ant_f: Fila en la que se encuentra la hormiga: Sin restricciones.
    - ant_c: Columna en la que se encuentra la hormiga: Sin restricciones.
    - matriz: Matriz por la que se desplaza la hormiga: Sin restricciones.
    - célula: Valor de la posición actual en la matriz: Sin restricciones.
    - revisor: Matriz que recuerda los valores de las celdas visitadas: Sin restricciones.
    Salidas:
    - Avance de la hormiga.
    Autores:
    Andrey Morales Reyes
    Alexei Quesada Leandro"""
    global ant_f, ant_c, matriz, célula, revisor
    nueva_f, nueva_c = siguiente(giro, célula, matriz)
    matriz[ant_f][ant_c] = (célula + 1) % len(colores)
    célula = matriz[nueva_f][nueva_c]
    matriz[nueva_f][nueva_c] = hormiga
    revisor[nueva_f][nueva_c] = célula
    ant_f = nueva_f
    ant_c = nueva_c

def generar_colores(reglas):
    """Procedimiento que se encarga de generar los colores y posición para cada letra del string recibido y separa las letras del string en una lista.
    Entradas y restricciones:
    - colores: Lista que contiene las posiciones para cada color de las letras del string.
    - color: Lista que contiene los colores para cada letra del string.
    - giro: Lista formada del string de Ls y Rs: Sin restricciones.
    Salidas:
    - Lista con colores.
    - Lista con letras del string.
    - Lista con posiciones del string.
    Autores:
    Andrey Morales Reyes
    Alexei Quesada Leandro"""
    global colores, color, giro
    string = reglas
    giro = []
    giro = list(string)
    colores = []
    for i in range(len(string)):
        colores.append(i)
    color = []
    for i in range(len(colores)):
        color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

def crear_matriz(filas, cols, valor):
    """Función que se encarga de generar las matrices.
    Entradas y restricciones:
    - filas: filas que tendrá la matriz
    - cols: Lista que contiene los colores para cada letra del string.
    - giro: Lista formada del string de Ls y Rs: Sin restricciones.
    Salidas:
    - Lista con colores.
    - Lista con letras del string.
    - Lista con posiciones del string.
    Autores:
    Andrey Morales Reyes
    Alexei Quesada Leandro"""
    M = []
    for f in range(filas):
        fila = []
        for c in range(cols):
            fila.append(valor)
        M.append(fila)
    return M

def init(filasi,columnas,reglas):
    global filas, cols, ant_f, ant_c
    global hormiga, dirección, matriz, color, giro, revisor
    filas = filasi
    cols = columnas
    generar_colores(reglas)
    matriz = crear_matriz(filas, cols, 0)
    revisor = crear_matriz(filas, cols, -2)
    ant_f = filas // 2
    ant_c = cols // 2
    hormiga = -1
    dirección = "U"
    célula = matriz[ant_f][ant_c]
    revisor[ant_f][ant_c] = célula
    matriz[ant_f][ant_c] = hormiga

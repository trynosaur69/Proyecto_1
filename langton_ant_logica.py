import random
import interfaz_inicial

matriz = []

ant_f = 0
ant_c = 0
hormiga = -1
dirección = "U"

célula = 0
colores = []
color = []
giro = []
revisor = []
L = {}
R = {}

def siguiente(giro, célula, matriz):
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
    global dirección
    if nueva_dirección in ("U", "D") and dirección in ("L", "R"):
        dirección = nueva_dirección
    elif nueva_dirección in ("L", "R") and dirección in ("U", "D"):
        dirección = nueva_dirección

def avanzar_hormiga():
    global ant_f, ant_c, matriz, célula, revisor
    nueva_f, nueva_c = siguiente(giro, célula, matriz)
    matriz[ant_f][ant_c] = (célula + 1) % len(colores)
    célula = matriz[nueva_f][nueva_c]
    matriz[nueva_f][nueva_c] = hormiga
    revisor[nueva_f][nueva_c] = célula
    ant_f = nueva_f
    ant_c = nueva_c

def generar_colores(reglas):
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

def crear_matriz_random(filas, cols):
    M = []
    for f in range(filas):
        fila = []
        for c in range(cols):
            fila.append(random.randint(0, len(colores) - 1))
        M.append(fila)
    return M

def crear_matriz(filas, cols, valor):
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

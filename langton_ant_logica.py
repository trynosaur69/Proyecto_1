import random
import Matrices

#Matriz
matriz = []
filas = 20
cols = 20

#Hormiga
ant_f = 0
ant_c = 0
hormiga = 2
dirección = "U" # U.Up D.Down R.Right L.Left

célula = 0 #Hay que determinar si está viva o muerta

def siguiente_posición(célula, matriz):
    if dirección == "R" and célula == 0 or dirección == "L" and célula == 1:
        cambiar_dirección("D")
        if ant_f + 1 == len(matriz):
            return 0, ant_c
        else:
            return ant_f + 1, ant_c
    elif dirección == "R" and célula == 1 or dirección == "L" and célula == 0:
        cambiar_dirección("U")
        if ant_f - 1 < 0:
            return len(matriz) - 1, ant_c
        else:
            return ant_f - 1, ant_c
    elif dirección == "U" and célula == 0 or dirección == "D" and célula == 1:
        cambiar_dirección("R")
        if ant_c + 1 == len(matriz[0]):
            return ant_f, 0
        else:
            return ant_f, ant_c + 1
    elif dirección == "U" and célula == 1 or dirección == "D" and célula == 0:
        cambiar_dirección("L")
        if ant_c - 1 < 0:
            return ant_f, len(matriz[0]) - 1
        else:
            return ant_f, ant_c - 1

#Puede ser que esta subrutina la podamos quitar
def cambiar_dirección(nueva_dirección):
    global dirección
    if nueva_dirección in ("U", "D") and dirección in ("L", "R"):
        dirección = nueva_dirección
    elif nueva_dirección in ("L", "R") and dirección in ("U", "D"):
        dirección = nueva_dirección

#Incompleto (más o menos una idea)
def avanzar():
    global ant_f, ant_c, matriz, célula
    nueva_f, nueva_c = siguiente_posición(célula, matriz)
    if matriz[nueva_f][nueva_c] == 0:
        matriz[ant_f][ant_c] = 1
    if matriz[nueva_f][nueva_c] == 1:
        matriz[ant_f][ant_c] = 0
    célula = matriz[nueva_f][nueva_c]
    matriz[nueva_f][nueva_c] = hormiga
    ant_f = nueva_f
    ant_c = nueva_c

def init():
    global filas, cols, ant_f, ant_c
    global hormiga, dirección, matriz
    filas = 50
    cols = 50
    matriz = Matrices.crear_matriz(filas, cols, 0)
    ant_f = filas // 2
    ant_c = cols // 2
    hormiga = 2
    dirección = "U"
    célula = matriz[ant_f][ant_c]
    matriz[ant_f][ant_c] = hormiga

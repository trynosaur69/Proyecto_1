#HAY QUE CAMBIAR LOS NOMBRES DE LAS SUBRUTINAS

import random
import Matrices

#Matriz
matriz = []
filas = 20
cols = 20

#Hormiga
ant_f = 0
ant_c = 0
hormiga = 1
dirección = "U" # U.Up D.Down R.Right L.Left

célula = 0 #Hay que determinar si está viva o muerta (Derecha o izquierda)(con  def generar_colores(n), talvez podemos determinarlo ahí)

def siguiente_posición(color, pos):
    if dirección == "R" and color == -1 or dirección == "L" and color == -2:
        cambiar_dirección("D")
        return ant_f + 1, ant_c
    elif dirección = "R" and color == -2 or dirección == "L" and color == -1:
        cambiar_dirección("U")
        return ant_f - 1, ant_c
    elif dirección == "U" and color == -1 or dirección == "D" and color == -2:
        cambiar_dirección("R")
        return ant_f, ant_c + 1
    elif dirección == "U" and color == -2 or dirección == "D" and color == -1:
        cambiar_dirección("L")
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
    global ant_f, ant_c, matriz
    nueva_f, nueva_c = siguiente_posición(color)
    if matriz[nueva_f][nueva_c] == blanco:
        matriz[ant_f][ant_c] = negro
    if matriz[nueva_f][nueva_c] == negro:
        matriz[ant_f][ant_c] = blanco
    matriz[nueva_f][nueva_c] = hormiga
    ant_f = nueva_f
    ant_c = nueva_c

def generar_colores(n):

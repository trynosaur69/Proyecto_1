from random import randint
from copy import deepcopy
import interfaz_inicial


def generar_matriz_aleatoria(filas, columnas):
    """Función que retorna una matriz de las dimensiones
    especificadas con valores enteros aleatorios de 0 o 1"""
    return [[randint(0, 1) for c in range(columnas)] for f in range(filas)]    
    
def generar_matriz_vacia(filas, columnas):
    return [[0 for c in range(columnas)] for f in range(filas)]
    

def obtener_vecinos(M, f, c):
    vecinos = []
    filas = len(M)
    columnas = len(M[0]) 
    
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue 
            nueva_f = (f + i) % filas
            nueva_c = (c + j) % columnas
            
            vecinos.append(M[nueva_f][nueva_c])
            
    return vecinos


def transicion_celula(estado, vecinos,birth,surv):
    sumatoria = vecinos.count(1)
    if estado == 0 and str(sumatoria) in birth:
        estado = 1
    elif estado == 1 and str(sumatoria) in surv:
        estado = 1
    else:
        estado = 0         
    return estado

def transicion(M,birth,surv):
    #deepcopy de matriz
    """Toma a la matriz completa y le aplica la función de
    transición a cada célula con su propio vecindario y deja
    el resultado en una matriz nueva."""
    nuevaM = deepcopy(M)
    for i in range(len(M)):
        for j in range(len(M[0])):
           vecinos = obtener_vecinos(M, i, j)
           transicion_celula(M[i][j], vecinos,birth,surv)
           nuevaM[i][j] = transicion_celula(M[i][j], vecinos,birth,surv)
     
    return nuevaM

  
  
  

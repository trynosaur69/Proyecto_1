from random import randint
from copy import deepcopy
import interfaz_inicial


def generar_matriz_aleatoria(filas, columnas):
    """Función que retorna una matriz de las dimensiones
    especificadas con valores enteros aleatorios de 0 o 1.
    Entradas y restricciones:
    - Filas: entero positivo mayor a 1.
    - Columnas: entero positivo mayor a 1.
    Salidas:
    - retorna matríz con valores 0 y 1.
    Autores:
    Andrey Morales Reyes
    Alexei Quesada Leandro
    """
    return [[randint(0, 1) for c in range(columnas)] for f in range(filas)]    
    
def generar_matriz_vacia(filas, columnas):
    """Función que retorna una matriz aleatoria con valores 0 usando las dimensiones \
    de las filas y las columnas introducidas por el usuario.
    Entradas y restricciones:
    - Filas: entero positivo mayor a 1.
    - Columnas: entero positivo mayor a 1.
    Salidas:
    - retorna matríz con valores 0.
    Autores:
    Andrey Morales Reyes
    Alexei Quesada Leandro"""
    return [[0 for c in range(columnas)] for f in range(filas)]
    

def obtener_vecinos(M, f, c):
    """ 
    Funcion que retorna el estado de los vecinos o sea su valor de 1 o 0.
    Entradas y restricciones:
    -M: matriz de igual cantidad de filas y columnas.
    -f: posición de filas, no tiene restricciones.
    -c: posición de columnas, no tiene restricciones.
    Salidas:
    -vecinos: retorna estado de vecinos.
    Autores:
    Andrey Morales Reyes
    Alexei Quesada Leandro
    """
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
    """
    Se encarga de cambiar el estado de la célula entre viva y muerta. Las reglas introducidas por el usuario determinan
    cuando nace una célula y cuando sobrevive.
    Entradas y restricciones:
    -Estado: entero sin restricciones.
    -Vecinos: lista de vecinos sin restricciones.
    -birth: lista de reglas para que una celula nazca sin restricciones.
    -surv: lista de reglas que definen si una celula sobrevive en la siguiente generación. sin restricciones.
    Autores:
    Andrey Morales Reyes
    Alexei Quesada Leandro
    """
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

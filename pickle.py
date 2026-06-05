#Creadores
#Andrey Morales Reyes
#Alexei Quesada Leandro

import colorsys
import pickle

#Gradientes
#hsv_to_rgb
h = 0
S = 1
V = 1
# i / 6
#rgb = hsv_to_rgb(_, 1, 1):




#pickle
#para escribir
archivo = open("datos.hormiga", "wb")
#lista
#diccionario ----> d
#matriz
#variables  #donde  #qué se guarda
pickle.dump(archivo, d)

#Para leer
archivo = open("datos.hormiga", "rb")
d = pickle.load(archivo)
archivo.close()

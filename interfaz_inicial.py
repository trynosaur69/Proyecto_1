from easygui import *
import easygui
#import life_like_gui
import sys


ret_val = msgbox("Bienvenido al programa principal, proximamente escoja su opcion preferida!")
if ret_val is None: 
    sys.exit(0)

msg ="Escoja la opción preferida?\nOr Press <cancel> to exit."
title = "Conway y Hormiga de Langton"
choices = ["Conway", "Langton Ant"]
hello = 0
while 1:
    choice = choicebox(msg, title, choices)
    if choice is None:
        sys.exit(0)
    if choice == "Conway":
        new_choice = enterbox("Diga sus reglas (Ejemplo: 1)")      
        if new_choice is None:
            continue    
        if new_choice == "1":
    if choice == "Hormiga de Langton":
        
        msgbox("Escogiste: {}".format(choice))


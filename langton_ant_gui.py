#Queda pendiente pickle y reiniciar con pausar y matriz 0

import pygame
import langton_ant_logica as Horlan
import pickle 

TICK = 100000

def main(reglas,filas,columnas,tamaño):
    """Programa principal de La Hormiga de Langton.
    Entradas y restricciones:
    - reglas: : Sin restricciones.
    - filas: : Sin restricciones.
    - columnas: : Sin restricciones.
    - tamaño: : Sin restricciones.
    Salidas:
    - Ninguna
    Autores:
    Andrey Morales Reyes
    Alexei Quesada Leandro"""
    pygame.init()
    Horlan.init(filas,columnas,reglas)
    ancho = Horlan.cols * tamaño
    alto = Horlan.filas * tamaño
    window = pygame.display.set_mode((ancho, alto))
    clock = pygame.time.Clock()
    loop = True
    pausado = False
    window.fill(Horlan.color[0])
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pausado = not pausado
                elif event.key == pygame.K_r:
                    window.fill(Horlan.color[0])
                    Horlan.init(filas,columnas,reglas)
                elif event.key == pygame.K_g:
                    estado_juego = {
                        "matriz": Horlan.matriz,
                        "revisor": Horlan.revisor,
                        "ant_f": Horlan.ant_f,
                        "ant_c": Horlan.ant_c,
                        "direccion": Horlan.dirección,
                        "celula": Horlan.célula,
                        "pausado": pausado
                    }
                    with open("partida_hormiga.pkl", "wb") as archivo:
                        pickle.dump(estado_juego, archivo)
                    print("Simulación guardada")
                elif event.key == pygame.K_c:
                    with open("partida_hormiga.pkl", "rb") as archivo:
                        estado_cargado = pickle.load(archivo)
                        Horlan.matriz = estado_cargado["matriz"]
                        Horlan.revisor = estado_cargado["revisor"]
                        Horlan.ant_f = estado_cargado["ant_f"]
                        Horlan.ant_c = estado_cargado["ant_c"]
                        Horlan.dirección = estado_cargado["direccion"]
                        Horlan.célula = estado_cargado["celula"]
                        pausado = estado_cargado["pausado"]
                        window.fill(Horlan.color[0])
                        print("Simulación cargada")
        for f in range(Horlan.filas):
            for c in range(Horlan.cols):
                x = c * tamaño
                y = f * tamaño
                if Horlan.matriz[f][c] in Horlan.colores and Horlan.revisor[f][c] != -2:
                    pygame.draw.rect(window, Horlan.color[Horlan.matriz[f][c]], (x, y, tamaño, tamaño))
                if Horlan.matriz[f][c] == -1:
                    pygame.draw.rect(window, (255, 0, 0), (x, y, tamaño, tamaño))
        if not pausado:
            Horlan.avanzar_hormiga()
        pygame.display.update()
        clock.tick(TICK)

            
    pygame.quit()

if __name__ == "__main__":
    main()


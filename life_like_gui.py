import pickle
import pygame
import life_like_logica as con



#tick no
tick = 10

def main(surv,birth,tamaño,filas,columnas):
    """Programa principal de simulador del juego de la vida de Conway.
    Entradas y restricciones:
    - birth : Sin restricciones.
    - surv : Sin restricciones. 
    - filas: : Sin restricciones.
    - columnas: : Sin restricciones.
    - tamaño: : Sin restricciones.
    Salidas:
    - Ninguna
    Autores:
    Andrey Morales Reyes
    Alexei Quesada Leandro"""
    pygame.init()
    clock = pygame.time.Clock()
    M = con.generar_matriz_aleatoria(filas, columnas)
    w, h = columnas * tamaño, filas * tamaño
    window = pygame.display.set_mode((w, h))
    loop = True
    pausa = False
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    pausa = not pausa
                elif keys[pygame.K_r]:
                    M = con.generar_matriz_aleatoria(filas, columnas)
                elif keys[pygame.K_b]:
                    M = con.generar_matriz_vacia(filas,columnas)
                elif keys[pygame.K_g]:
                    estado_conway = {
                        "matriz": M,
                        "pausa": pausa
                    }
                    with open("partida_conway.pkl", "wb") as archivo:
                        pickle.dump(estado_conway, archivo)
                    print("Simulación de Conway guardada")
                elif keys[pygame.K_c]:
                    with open("partida_conway.pkl", "rb") as archivo:
                        estado_cargado = pickle.load(archivo)
                    M = estado_cargado["matriz"]
                    pausa = estado_cargado["pausa"]
                    print("Simulación cargada")
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons = pygame.mouse.get_pressed()
                x, y = pygame.mouse.get_pos()
                if buttons[0]:
                    f = y // tamaño
                    c = x // tamaño
                    M[f][c] = (M[f][c] + 1) % 2
                    
        window.fill((0, 0, 0))
        for f in range(filas):
            for c in range(columnas):
                if M[f][c] == 1:
                    x = c * tamaño
                    y = f * tamaño
                    pygame.draw.rect(window, (0, 255, 128), (x, y, tamaño, tamaño))
        if not pausa:
            M = con.transicion(M,birth,surv)
        pygame.display.update()
        clock.tick(10)
    pygame.quit()

if __name__ == "__main__":
    main()


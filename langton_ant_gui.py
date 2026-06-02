import pygame
import Hormiga_de_Langton_Lógica as Horlan

TAM = 10
TICK = 1

def main():
    pygame.init()
    Horlan.init()
    ancho = Horlan.cols * TAM
    alto = Horlan.filas * TAM
    window = pygame.display.set_mode((ancho, alto))
    clock = pygame.time.Clock()
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
        window.fill((0, 0, 0))
        for f in range(Horlan.filas):
            for c in range(Horlan.cols):
                x = c * TAM
                y = f * TAM
                if Horlan.matriz[f][c] == 0:
                    pygame.draw.rect(window, (0, 0, 0), (x, y, TAM, TAM))
                elif Horlan.matriz[f][c] == 1:
                    pygame.draw.rect(window, (255, 255, 255), (x, y, TAM, TAM))
                elif Horlan.matriz[f][c] == 2:
                    pygame.draw.rect(window, (255, 0, 0), (x, y, TAM, TAM))
        Horlan.avanzar()
        pygame.display.update()
        clock.tick(TICK)

            
    pygame.quit()

if __name__ == "__main__":
    main()


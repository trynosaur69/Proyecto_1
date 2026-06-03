import pygame
import Hormiga_de_Langton_Lógica as Horlan

TAM = 3
TICK = 100000

def main():
    pygame.init()
    Horlan.init()
    ancho = Horlan.cols * TAM
    alto = Horlan.filas * TAM
    window = pygame.display.set_mode((ancho, alto))
    clock = pygame.time.Clock()
    loop = True
    window.fill(Horlan.color[0])
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
        for f in range(Horlan.filas):
            for c in range(Horlan.cols):
                x = c * TAM
                y = f * TAM
                if Horlan.matriz[f][c] in Horlan.colores and Horlan.revisor[f][c] != -2:
                    pygame.draw.rect(window, Horlan.color[Horlan.matriz[f][c]], (x, y, TAM, TAM))
                if Horlan.matriz[f][c] == -1:
                    pygame.draw.rect(window, (255, 0, 0), (x, y, TAM, TAM))
        Horlan.avanzar()
        pygame.display.update()
        clock.tick(TICK)

            
    pygame.quit()

if __name__ == "__main__":
    main()
    

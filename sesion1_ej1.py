import pygame
pygame.init()
ventana = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Mi primer programa")
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    ventana.fill(color=((0, 255, 0)))
    pygame.display.flip()
pygame.quit()
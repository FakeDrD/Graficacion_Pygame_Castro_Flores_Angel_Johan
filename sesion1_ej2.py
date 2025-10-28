import pygame
pygame.init()
ventana = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mi primer programa")
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    ventana.fill(color=((0, 255, 0)))
    pygame.display.flip()
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_ESCAPE:
            corriendo = False
pygame.quit()
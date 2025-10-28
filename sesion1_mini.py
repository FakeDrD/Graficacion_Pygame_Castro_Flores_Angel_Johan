import pygame
pygame.init()
ventana = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mi primer programa")
color_fondo = ("white")
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                corriendo = False
            if evento.key == pygame.K_c:
                if color_fondo == "blue":
                    color_fondo = "white"
                else:
                    color_fondo = "blue"
    ventana.fill(color=(color_fondo))
    pygame.display.flip()        
            
pygame.quit()
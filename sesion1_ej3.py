import pygame
pygame.init()
ventana = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sesion1_ej3")
reloj = pygame.time.Clock()
corriendo = True
contador=0
while corriendo:
    contador+=1
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    ventana.fill(color=((0, 255, 0)))
    pygame.display.flip()
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_ESCAPE:
            corriendo = False
    if contador <= 300:
        print(f"Frame: {contador}.")
    else:
        corriendo = False
    reloj.tick(60)  # 60 FPS 
pygame.quit()
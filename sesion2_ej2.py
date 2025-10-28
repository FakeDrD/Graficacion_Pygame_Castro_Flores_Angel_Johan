import pygame
pygame.init()
ventana = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Mi primer programa")
corriendo = True
x=100
ventana.fill(color=(("white")))
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                corriendo = False
        for i in range(5):
            
            if i==0:
                pygame.draw.circle(ventana, ("red"), (200, 200), x)
            if i==1:
                pygame.draw.circle(ventana, ("blue"), (200, 200), x)
            if i==2:
                pygame.draw.circle(ventana, ("green"), (200, 200), x)
            if i==3:
                pygame.draw.circle(ventana, ("yellow"), (200, 200), x)
            if i==4:
                pygame.draw.circle(ventana, ("purple"), (200, 200), x)
            pygame.display.flip()    
            x-=20
pygame.quit()
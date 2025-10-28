import pygame
pygame.init()
ventana = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Mi primer programa")
corriendo = True
x=0
y=0
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                corriendo = False
        for i in range(8):
            x=0
            for j in range(8):
                if (i+j)%2==0:
                    pygame.draw.rect(ventana, ("black"), ( x, y, 50, 50))
                else:   
                    pygame.draw.rect(ventana, ("white"), ( x, y, 50, 50))    
                x+=50      
                pygame.display.flip()       
            y+=50

pygame.quit()
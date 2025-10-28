import pygame
import sys

# --- Constantes ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TITULO_VENTANA = "Movimiento con Límites"

COLOR_FONDO = (0, 0, 0) # Negro
COLOR_NORMAL = (0, 255, 0) # Verde
COLOR_BORDE = (255, 0, 0) # Rojo[span_21](end_span)

VELOCIDAD = 5

# --- Inicialización ---
pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption(TITULO_VENTANA)
reloj = pygame.time.Clock()

# Definir el rectángulo
rectangulo = pygame.Rect(375, 275, 50, 50)
color_actual = COLOR_NORMAL

# --- Bucle Principal ---
ejecutando = True
while ejecutando:
    # --- Manejo de Eventos ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False

    # --- Lógica de Movimiento ---
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        rectangulo.x -= VELOCIDAD
    if teclas[pygame.K_RIGHT]:
        rectangulo.x += VELOCIDAD
    if teclas[pygame.K_UP]:
        rectangulo.y -= VELOCIDAD
    if teclas[pygame.K_DOWN]:
        rectangulo.y += VELOCIDAD

    # [span_22](start_span)Asegurarse de que el rectángulo no se salga de la ventana[span_22](end_span)
    if rectangulo.left < 0:
        rectangulo.left = 0
    if rectangulo.right > ANCHO_VENTANA:
        rectangulo.right = ANCHO_VENTANA
    if rectangulo.top < 0:
        rectangulo.top = 0
    if rectangulo.bottom > ALTO_VENTANA:
        rectangulo.bottom = ALTO_VENTANA

    # [span_23](start_span)Comprobar si toca los bordes y cambiar de color[span_23](end_span)
    toca_borde = (rectangulo.left == 0 or 
                  rectangulo.right == ANCHO_VENTANA or 
                  rectangulo.top == 0 or 
                  rectangulo.bottom == ALTO_VENTANA)

    if toca_borde:
        color_actual = COLOR_BORDE
    else:
        color_actual = COLOR_NORMAL

    # --- Lógica de Dibujo ---
    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(pantalla, color_actual, rectangulo)

    # --- Actualizar Pantalla ---
    pygame.display.flip()
    
    # Controlar los FPS
    reloj.tick(60)

# --- Salir ---
pygame.quit()
sys.exit()
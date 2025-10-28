import pygame
import sys
import math

# --- Constantes ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TITULO_VENTANA = "Trayectoria Predefinida"

COLOR_FONDO = (0, 0, 0)
COLOR_RECT = (0, 150, 255)

CENTRO_X = 400 
CENTRO_Y = 300 
RADIO = 150
VELOCIDAD_ANGULAR = 0.03

# --- Inicialización ---
pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption(TITULO_VENTANA)
reloj = pygame.time.Clock()

# Definir el rectángulo
rectangulo = pygame.Rect(0, 0, 40, 40)
angulo = 0

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
    # Actualizar el ángulo
    angulo += VELOCIDAD_ANGULAR

    # [span_26](start_span)Calcular la nueva posición usando trigonometría[span_26](end_span)
    # x = centro_x + cos(angulo) * radio
    # y = centro_y + sin(angulo) * radio
    nueva_x = CENTRO_X + math.cos(angulo) * RADIO
    nueva_y = CENTRO_Y + math.sin(angulo) * RADIO
    
    # Actualizar la posición central del rectángulo
    rectangulo.center = (nueva_x, nueva_y)

    # --- Lógica de Dibujo ---
    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(pantalla, COLOR_RECT, rectangulo)

    # --- Actualizar Pantalla ---
    pygame.display.flip()
    
    # Controlar los FPS
    reloj.tick(60)

# --- Salir ---
pygame.quit()
sys.exit()
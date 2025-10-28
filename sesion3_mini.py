import pygame
import sys

# --- Constantes ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TITULO_VENTANA = "Mini-proyecto Sesión 3: Rastro"

COLOR_FONDO = (0, 0, 0)
COLOR_RECT = (255, 0, 0)
COLOR_RASTRO = (0, 255, 255) # Cyan
RADIO_RASTRO = 5
LIMITE_RASTRO = 150 # Número máximo de círculos en el rastro

VELOCIDAD = 7

# --- Inicialización ---
pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption(TITULO_VENTANA)
reloj = pygame.time.Clock()

# Definir el rectángulo
rectangulo = pygame.Rect(375, 275, 50, 50)

# [span_27](start_span)Lista para almacenar las posiciones del rastro[span_27](end_span)
posiciones_rastro = []

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
    # [span_28](start_span)Mover el rectángulo con el teclado[span_28](end_span)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        rectangulo.x -= VELOCIDAD
    if teclas[pygame.K_RIGHT]:
        rectangulo.x += VELOCIDAD
    if teclas[pygame.K_UP]:
        rectangulo.y -= VELOCIDAD
    if teclas[pygame.K_DOWN]:
        rectangulo.y += VELOCIDAD

    # Mantener dentro de la pantalla
    rectangulo.clamp_ip(pantalla.get_rect())

    # [span_29](start_span)Añadir la posición central actual a la lista de rastro[span_29](end_span)
    posiciones_rastro.append(rectangulo.center)

    # Limitar la longitud del rastro
    if len(posiciones_rastro) > LIMITE_RASTRO:
        posiciones_rastro.pop(0) # Elimina el círculo más antiguo

    # --- Lógica de Dibujo ---
    pantalla.fill(COLOR_FONDO)

    # [span_30](start_span)Dibujar el rastro[span_30](end_span)
    for pos in posiciones_rastro:
        pygame.draw.circle(pantalla, COLOR_RASTRO, pos, RADIO_RASTRO)

    # Dibujar el rectángulo principal
    pygame.draw.rect(pantalla, COLOR_RECT, rectangulo)

    # --- Actualizar Pantalla ---
    pygame.display.flip()
    
    # Controlar los FPS
    reloj.tick(60)

# --- Salir ---
pygame.quit()
sys.exit()
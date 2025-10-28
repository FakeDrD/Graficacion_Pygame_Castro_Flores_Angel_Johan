import pygame
import sys

# --- Constantes ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TITULO_VENTANA = "Mini-proyecto Sesión 2: La Casa"

COLOR_FONDO = ("Black") # Negro
COLOR_TEJADO = ("Purple")   # Morado
COLOR_VENTANA = ("Yellow")  # Amarillo

COLOR_ROJO = (255, 0, 0)
COLOR_AZUL = (0, 0, 255)
COLOR_DEFAULT = (200, 200, 200) # Gris claro

# --- Inicialización ---
pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption(TITULO_VENTANA)

# Variable para el color actual de la casa
color_casa_actual = COLOR_DEFAULT

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
            
            # [span_18](start_span)Cambiar color con 'R'[span_18](end_span)
            if evento.key == pygame.K_r:
                color_casa_actual = COLOR_ROJO
            # [span_19](start_span)Cambiar color con 'B'[span_19](end_span)
            if evento.key == pygame.K_b:
                color_casa_actual = COLOR_AZUL

    # --- Lógica de Dibujo ---
    pantalla.fill(COLOR_FONDO)

    # [span_20](start_span)Dibujar las primitivas que forman la casa[span_20](end_span)

    # Cuerpo (Rectángulo) - Usa el color variable
    pygame.draw.rect(pantalla, color_casa_actual, (300, 300, 200, 200))

    # Tejado (Triángulo/Polígono)
    puntos_tejado = [(280, 300), (520, 300), (400, 200)]
    pygame.draw.polygon(pantalla, COLOR_TEJADO, puntos_tejado)

    # Ventanas (Círculos)
    pygame.draw.circle(pantalla, COLOR_VENTANA, (350, 370), 30)
    pygame.draw.circle(pantalla, COLOR_VENTANA, (450, 370), 30)

    # --- Actualizar Pantalla ---
    pygame.display.flip()

# --- Salir ---
pygame.quit()
sys.exit()
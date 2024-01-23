
import random
import pygame

# Definimos la ventana y algunas constantes
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
BG_COLOR = (255, 255, 255)
SNAKE_COLOR = (0, 255, 0)
APPLE_COLOR = (255, 0, 0)
FONT_COLOR = (0, 0, 0)

# Inicializamos Pygame
pygame.init()

# Creamos la ventana
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

# Creamos el reloj
clock = pygame.time.Clock()

# Definimos algunas funciones útiles
def draw_cell(x, y, color):
    pygame.draw.rect(window, color, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_text(text, font_size, x, y):
    font = pygame.font.Font(pygame.font.get_default_font(), font_size)
    surface = font.render(text, True, FONT_COLOR)
    window.blit(surface, (x, y))

def get_random_position():
    return (
        random.randint(0, WINDOW_WIDTH//CELL_SIZE-1),
        random.randint(0, WINDOW_HEIGHT//CELL_SIZE-1)
    )

# Inicializamos el juego
snake = [(10, 10)]
direction = (1, 0)
apple_position = get_random_position()
score = 0

# Bucle principal del juego
running = True
while running:
    # Eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    # Actualizamos la lógica del juego
    head_x, head_y = snake[-1]
    new_head_x = head_x + direction[0]
    new_head_y = head_y + direction[1]

    # Comprobamos si hemos chocado con la pared
    if new_head_x < 0 or new_head_x >= WINDOW_WIDTH//CELL_SIZE or \
       new_head_y < 0 or new_head_y >= WINDOW_HEIGHT//CELL_SIZE:
        running = False

    # Comprobamos si hemos chocado con la serpiente
    elif (new_head_x, new_head_y) in snake:
        running = False

    # Comprobamos si hemos comido una manzana
    elif (new_head_x, new_head_y) == apple_position:
        snake.append((new_head_x, new_head_y))
        apple_position = get_random_position()
        score += 1

    # Si no, simplemente avanzamos un paso
    else:
        snake.pop(0)
        snake.append((new_head_x, new_head_y))

    # Dibujamos el juego
    window.fill(BG_COLOR)

    for x, y in snake:
        draw_cell(x, y, SNAKE_COLOR)

    draw_cell(apple_position[0], apple_position[1], APPLE_COLOR)

    draw_text(f"Score: {score}", 30, 10, 10)

    # Actualizamos la pantalla
    pygame.display.flip()

    # Controlamos la velocidad del juego
    clock.tick(10)

# Salimos del juego
pygame.quit()

import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Classic Snake")

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GREEN = (0, 180, 0)
RED = (220, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
running = True
game_over = False

snake = [
    [100, 100],
    [80, 100],
    [60, 100]
]

direction = "RIGHT"

food = [
    random.randrange(0, WIDTH, CELL_SIZE),
    random.randrange(0, HEIGHT, CELL_SIZE)
]

MOVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_EVENT, 150)

font = pygame.font.Font(None, 50)

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if not game_over and event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"

            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"

            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"

            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

        if event.type == MOVE_EVENT and not game_over:

            head = snake[0].copy()

            if direction == "UP":
                head[1] -= CELL_SIZE
            elif direction == "DOWN":
                head[1] += CELL_SIZE
            elif direction == "LEFT":
                head[0] -= CELL_SIZE
            elif direction == "RIGHT":
                head[0] += CELL_SIZE

            # Wall collision
            if (
                head[0] < 0 or
                head[0] >= WIDTH or
                head[1] < 0 or
                head[1] >= HEIGHT
            ):
                game_over = True

            # Self collision
            elif head in snake[:-1]:
                game_over = True

            else:
                snake.insert(0, head)

                if head == food:

                    empty_cells = [
                        [x, y]
                        for x in range(0, WIDTH, CELL_SIZE)
                        for y in range(0, HEIGHT, CELL_SIZE)
                        if [x, y] not in snake
                    ]

                    if empty_cells:
                        food = random.choice(empty_cells)

                else:
                    snake.pop()

    screen.fill(WHITE)

    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))

    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

    pygame.draw.rect(
        screen, RED,
        (food[0], food[1], CELL_SIZE, CELL_SIZE)
    )

    for segment in snake:
        pygame.draw.rect(
            screen, GREEN,
            (segment[0], segment[1], CELL_SIZE, CELL_SIZE)
        )

    if game_over:
        text = font.render("GAME OVER", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    pygame.display.update()
    clock.tick(60)

pygame.time.set_timer(MOVE_EVENT, 0)
pygame.quit()
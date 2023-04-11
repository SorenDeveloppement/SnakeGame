import pygame
import time
import random
from PIL import Image, ImageFilter

rr = False
gr = False
br = False


def rainbowColor(color):
    global rr, gr, br
    red, green, blue = color

    if rr:
        if red <= 1:
            rr = False
            red = 2
        else:
            red -= 1
    else:
        if red >= 254:
            rr = True
            red = 253
        else:
            red += 1

    if gr:
        if green <= 1:
            gr = False
            green = 2
        else:
            green -= 1
    else:
        if green >= 254:
            gr = True
            green = 253
        else:
            green += 1

    if br:
        if blue <= 1:
            br = False
            blue = 2
        else:
            blue -= 1
    else:
        if blue >= 254:
            br = True
            blue = 253
        else:
            blue += 1

    return red, green, blue


# Colors
BACKGROUND = (10, 10, 10)
SNAKE_COLOR = (0, 177, 255)
APPLE_COLOR = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
WHITE_SMOKE = (200, 200, 200)

# Pygame variables
WIDTH = 800
HEIGHT = 600

# Game variables
SNAKE_SIZE = 3
GRID_SIZE = 20
SNAKE = [[20, 13], [20, 14], [20, 15]]
SLEEP_TIME = 0.1
DIRECTION = [0, 1]
APPLE = [random.randint(1, 39), random.randint(1, 29)]
SCORE = 0


def main():
    global SNAKE_SIZE, SNAKE_COLOR, APPLE, DIRECTION, SCORE, APPLE_COLOR

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Gala_Glow's Snake Game")

    screen.fill(BACKGROUND)

    pygame.display.flip()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    DIRECTION = [0, -1]
                if event.key == pygame.K_DOWN:
                    DIRECTION = [0, 1]
                if event.key == pygame.K_RIGHT:
                    DIRECTION = [1, 0]
                if event.key == pygame.K_LEFT:
                    DIRECTION = [-1, 0]

        screen.fill(BACKGROUND)

        # SNAKE Eat APPLE
        if SNAKE[SNAKE_SIZE - 1][0] == APPLE[0] and SNAKE[SNAKE_SIZE - 1][1] == APPLE[1]:
            APPLE_COLOR = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            generate_apple()
            SNAKE.insert(0, [SNAKE[0][0] + DIRECTION[0], SNAKE[0][1] + DIRECTION[1]])
            SNAKE_SIZE += 1
            SCORE += 1

        # SNAKE Direction
        if DIRECTION is not None:
            SNAKE.append([SNAKE[SNAKE_SIZE - 1][0] + DIRECTION[0], SNAKE[SNAKE_SIZE - 1][1] + DIRECTION[1]])
            SNAKE.pop(0)

        # SNAKE Out Of Map
        if SNAKE[SNAKE_SIZE - 1][0] <= -1 or SNAKE[SNAKE_SIZE - 1][1] <= -1 or SNAKE[SNAKE_SIZE - 1][0] >= 40 or \
                SNAKE[SNAKE_SIZE - 1][1] >= 30:
            pygame.quit()
            return

        # SNAKE Collisions
        w_head = SNAKE[:-1]
        if SNAKE[SNAKE_SIZE - 1] in w_head:
            pygame.quit()
            return

        pygame.draw.rect(screen, APPLE_COLOR, (APPLE[0] * GRID_SIZE, APPLE[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        for i in range(SNAKE_SIZE):
            SNAKE_COLOR = rainbowColor(SNAKE_COLOR)
            pygame.draw.rect(screen, SNAKE_COLOR,
                             (SNAKE[i][0] * GRID_SIZE, SNAKE[i][1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        text = pygame.font.SysFont('Consolas', 75).render(str(SCORE), True, WHITE_SMOKE)
        text_rect = text.get_rect(center=(WIDTH / 2, 50))
        screen.blit(text, text_rect)

        pygame.display.update()

        time.sleep(SLEEP_TIME)


def generate_apple():
    global APPLE

    x = random.randint(1, 39)
    y = random.randint(1, 29)
    if [x, y] not in SNAKE:
        APPLE = [x, y]
    else:
        generate_apple()


if __name__ == '__main__':
    main()

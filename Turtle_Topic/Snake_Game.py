import pygame
import random

# Initialize pygame
pygame.init()

# Set width and height
width, height = 600, 600
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("----------Snake Game----------")

# Initial snake position and movement
snake_x, snake_y = width // 2, height // 2
change_x, change_y = 10, 0  # Start moving right

# Food position (aligned to grid of 10)
food_x = random.randrange(0, width, 10)
food_y = random.randrange(0, height, 10)

snake_body = [(snake_x, snake_y)]
clock = pygame.time.Clock()

def display_snake_and_food():
    global snake_x, snake_y, food_x, food_y

    snake_x = (snake_x + change_x) % width
    snake_y = (snake_y + change_y) % height

    # Check self collision
    if (snake_x, snake_y) in snake_body[1:]:
        print("Game Over")
        pygame.quit()
        quit()

    snake_body.append((snake_x, snake_y))

    # Check if food is eaten
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randrange(0, width, 10)
        food_y = random.randrange(0, height, 10)
    else:
        snake_body.pop(0)

    # Drawing
    game_screen.fill((0, 0, 0))  # Black background
    pygame.draw.rect(game_screen, (0, 255, 0), [food_x, food_y, 10, 10])  # Green food
    for x, y in snake_body:
        pygame.draw.rect(game_screen, (255, 255, 255), [x, y, 10, 10])  # White snake
    pygame.display.update()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and change_x == 0:
                change_x = -10
                change_y = 0
            elif event.key == pygame.K_RIGHT and change_x == 0:
                change_x = 10
                change_y = 0
            elif event.key == pygame.K_UP and change_y == 0:
                change_y = -10
                change_x = 0
            elif event.key == pygame.K_DOWN and change_y == 0:
                change_y = 10
                change_x = 0

    display_snake_and_food()
    clock.tick(10)

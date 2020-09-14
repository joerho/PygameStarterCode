import pygame
import random

######################################################################
# basic intialization
pygame.init()

# screen size setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# screen title setting
pygame.display.set_caption("Game name")

# FPS
clock = pygame.time.Clock()
######################################################################

# 1. user game initialization (background, image loading, speed, font)
background = pygame.image.load(
    "C:/Users/sam/Desktop/Programming/pythonworkspace/pygame_basic/background.png")
character = pygame.image.load(
    "C:/Users/sam/Desktop/Programming/pythonworkspace/pygame_basic/character.png")
enemy = pygame.image.load(
    "C:/Users/sam/Desktop/Programming/pythonworkspace/pygame_basic/enemy.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = -enemy_height

character_dx = 0
charcter_dy = 0

enemy_dx = 0
enemy_dy = 0

character_speed = 0.6
enemy_speed = 0.6


# event loop
running = True
while running:
    dt = clock.tick(30)  # set FPS

    # 2. handle event (keyboard, mouse)
    for event in pygame.event.get():  # catching the event
        if event.type == pygame.QUIT:  # if event is quit
            running = False  # set running to false

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_dx -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_dx += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_dx = 0

    # 3. character location
    character_x_pos += character_dx * dt
    enemy_y_pos += enemy_speed * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if enemy_y_pos >= screen_height:
        enemy_y_pos = -enemy_height
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    # 4. collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("collided")
        running = False

    # 5. draw
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()  # redraw display


# pygame quit
pygame.quit()

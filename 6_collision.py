import pygame

pygame.init()

# screen size setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# screen title setting
pygame.display.set_caption("Joe's Game")

# FPS
clock = pygame.time.Clock()

# load background
background = pygame.image.load(
    "C:/Users/sam/Desktop/Programming/pythonworkspace/pygame_basic/background.png")

# load sprite
character = pygame.image.load(
    "C:/Users/sam/Desktop/Programming/pythonworkspace/pygame_basic/character.png")
character_size = character.get_rect().size  # get image size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - (character_width / 2)
character_y_pos = screen_height - character_height

# movement amount
to_x = 0
to_y = 0

# movement speed
character_speed = 0.6

# load enemy sprite
enemy = pygame.image.load(
    "C:/Users/sam/Desktop/Programming/pythonworkspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size  # get image size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)
# event loop
running = True
while running:
    dt = clock.tick(60)  # set FPS

    for event in pygame.event.get():  # catching the event
        if event.type == pygame.QUIT:  # if event is quit
            running = False  # set running to false
        if event.type == pygame.KEYDOWN:  # key pressed
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # rect info update for collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # collision check
    if character_rect.colliderect(enemy_rect):
        print("collided")
        running = False

    screen.blit(background, (0, 0))  # draw background
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    pygame.display.update()  # redraw display


# pygame quit
pygame.quit()

import pygame

pygame.init()

# screen size setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# screen title setting
pygame.display.set_caption("Joe's Game")

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
character_y_pos = screen_height - character_width

to_x = 0
to_y = 0
# event loop
running = True
while running:
    for event in pygame.event.get():  # catching the event
        if event.type == pygame.QUIT:  # if event is quit
            running = False  # set running to false
        if event.type == pygame.KEYDOWN:  # key pressed
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))  # draw background
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()  # redraw display


# pygame quit
pygame.quit()

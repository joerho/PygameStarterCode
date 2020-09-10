import pygame

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

# event loop
running = True
while running:
    dt = clock.tick(60)  # set FPS

    # 2. handle event (keyboard, mouse)
    for event in pygame.event.get():  # catching the event
        if event.type == pygame.QUIT:  # if event is quit
            running = False  # set running to false

    # 3. character location

    # 4. collision

    # 5. draw

    pygame.display.update()  # redraw display


# pygame quit
pygame.quit()

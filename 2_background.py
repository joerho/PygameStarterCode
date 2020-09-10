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

# event loop
running = True
while running:
    for event in pygame.event.get():  # catching the event
        if event.type == pygame.QUIT:  # if event is quit
            running = False  # set running to false

    screen.blit(background, (0, 0))  # draw background
    pygame.display.update()  # redraw display


# pygame quit
pygame.quit()

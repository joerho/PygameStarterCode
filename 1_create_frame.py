import pygame

pygame.init()

# screen size setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# screen title setting
pygame.display.set_caption("Joe's Game")

running = True
while running:
    for event in pygame.event.get():  # catching the event
        if event.type == pygame.QUIT:  # if event is quit
            running = False  # set running to false


# pygame quit
pygame.quit()

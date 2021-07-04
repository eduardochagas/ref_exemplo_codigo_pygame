import pygame

RED = (200, 0, 0)
GREEN = (0, 200 , 0)
BLUE = (0, 0, 200)
BLACK = (0, 0, 0)

FPS = 60

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           exit()

    pygame.display.update()
    clock.tick(FPS)

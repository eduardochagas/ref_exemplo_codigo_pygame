import pygame

RED = (200, 0, 0)
GREEN = (0, 200 , 0)
BLUE = (0, 0, 200)

FPS = 60

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

rect = pygame.Rect(60, 60, 30, 30)
x = 0
y = 0
width = 0
height = 0


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                x += 110
                y += 110
                width += 50
                height += 50
                #########################################
                # O método: update() de um objeto rect muda a posição (x,y) e
                # a largura e altura (width, height) desse objeto rect na tela.
                #
                rect.update(x, y, width, height)

    #####################################
    # Desenhando o rect (Vermelho)
    #
    pygame.draw.rect(screen, RED, rect)

    pygame.display.update()
    clock.tick(FPS)

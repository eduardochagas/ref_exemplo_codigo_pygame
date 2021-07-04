import pygame

RED = (200, 0, 0)
GREEN = (0, 200 , 0)
BLUE = (0, 0, 200)

FPS = 60

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

#######################################
#  criando o primeiro rect...
#
rect = pygame.Rect(30, 30, 30, 30)
######################################
#  Criando uma cópia do primeiro rect, gerando um novo rect...
#
rect_copy = rect.copy()
rect_copy.topleft = (100, 150) # definindo uma nova posição para o rect cópia...

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           exit()

    ######################################
    # Desenhando o primeiro rect criado....
    pygame.draw.rect(screen, RED, rect)
    ###########################################
    # Desenhando o SEGUNDO RECT (RECT CÓPIA)
    #   OBS: o rect cópia foi desenhado em uma posição diferente na tela
    #   pq definimos uma nova posição para ele (rect_copy.topleft = (100, 150)),
    #   caso contrário, o rect cópia seria desenhado
    #   exatamente em cima do primeiro rect. 
    pygame.draw.rect(screen, BLUE, rect_copy)

    pygame.display.update()
    clock.tick(FPS)

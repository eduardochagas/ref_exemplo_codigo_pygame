import pygame

RED = (200, 0, 0)
GREEN = (0, 200 , 0)
BLUE = (0, 0, 200)
YELLOW = (200, 200, 0)
BLACK = (0, 0, 0)

FPS = 60

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

######################################
# criando o rect1 (VERDE)
#
surf = pygame.Surface((80, 80))
surf.fill(GREEN)
rect1 = surf.get_rect()
rect1.x = 90
rect1.y = 90

######################################
# criando o rect2 (VERMELHO)
#
surf2 = pygame.Surface((20, 20))
surf2.fill(RED)
rect2 = surf.get_rect()
rect2.x = 20
rect2.y = 20


##########################################
# criando o rect3 (cor AMARELO)
#
rect3 = pygame.Rect(430, 80, 70, 70)
##########################################
# criando o rect4 (cor AZUL)
#
rect4 = pygame.Rect(300, 20, 100, 100)

running = True
while running:

    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                ##################################
                # insere o rect1 dentro do rect2
                #   OBS: o rect1 é inserido no rect2 a partir da posição inicial (x,y)
                #   do rect2.
                #
                rect2.clamp_ip(rect1)

            if event.key == pygame.K_d:
                ##################################
                # insere o rect3 dentro do rect4
                #   OBS: quando passamos UM RECT PARA DENTRO
                #   DE OUTRO RECT (usando o método: clamp_ip()), SE
                #   O RECT PASSADO (NO CASO, rect3 (AMARELO)) FOR MAIOR
                #   QUE O RECT QUE RECEBE (NO CASO, rect4 (VERMELHO)), O RECT PASSADO (NO CASO, rect3 (AMARELO))
                #   fica POSICIONADO NO CENTRO DO RECT QUE RECEBE O RECT PASSSADO (NO CASO, rect4).
                #
                rect4.clamp_ip(rect3)

    #####################################
    # insere na tela o rect1 (Verde)
    #
    screen.blit(surf, (rect1.x, rect1.y))
    #####################################
    # insere na tela o rect2 (Vermelho)
    #
    screen.blit(surf2, (rect2.x, rect2.y))


    #######################################
    # insere na tela o rect3 (AMARELO)
    #
    pygame.draw.rect(screen, YELLOW, rect3)
    #######################################
    # insere na tela o rect4 (VERMELHO)
    #
    pygame.draw.rect(screen, RED, rect4)

    pygame.display.update()
    clock.tick(FPS)

import pygame

RED = (200, 0, 0)
GREEN = (0, 200 , 0)
BLUE = (0, 0, 200)
YELLOW = (200, 200, 0)
BLACK = (0, 0, 0)

FPS = 60

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

###################################
# Exemplo usando superfície e gerando a área retângular
#
surf1 = pygame.Surface((30, 30))
surf1.fill(RED)
rect_surf1 = surf1.get_rect()
rect_surf1.x = 30
rect_surf1.y = 30

surf2 = pygame.Surface((50, 50))
surf2.fill(GREEN)
rect_surf2 = surf2.get_rect()
rect_surf2.x = 100 #250
rect_surf2.y = 30 #50

surf3 = pygame.Surface((20, 20))
surf3.fill(YELLOW)
rect_surf3 = surf3.get_rect()
active1 = False

##########################################
# Exemplo usando somente o objeto Rect (área retângular)
#
rect1 = pygame.Rect(200, 30, 30, 30)
rect2 = pygame.Rect(250, 50, 50, 50)
rect3 = pygame.Rect(0, 0, 0, 0)
active2 = False


running = True
while running:

    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           exit()

        if event.type == pygame.KEYDOWN:
            ###################################
            # Executando Exemplo usando superfície e gerando a área retângular
            #
            if event.key == pygame.K_a:
                ##################################
                # o método: clamp_ip() de um objeto rect INSERE UM RETÂNGULO (rect_surf2)
                # DENTRO DE OUTRO OBJETO RETÂNGULAR (rect_surf1)
                #
                rect_surf1.clamp_ip(rect_surf2)

            if event.key == pygame.K_s:
                ##############################################
                # o método: clip() de um objeto rect PEGA O OBJETO RECT INSERIDO DENTRO
                # DE OUTRO OBJETO RECT (pega o: rect_surf2 QUE ESTÁ DENTRO DE: rect_surf1), E
                # RETORNA ESSE OBJETO (rect_surf2).
                #
                rect_surf3 = rect_surf1.clip(rect_surf2)
                rect_surf3.x = 30 # inserindo o objeto retornado (rect_surf2) em uma nova posição em: x
                rect_surf3.y = 30 # inserindo o objeto retornado (rect_surf2) em uma nova posição em: y
                print(rect_surf3)
                active1 = True

            ###################################
            # Exemplo usando somente o objeto Rect (área retângular)
            #
            if event.key == pygame.K_z:
                ##################################
                # o método: clamp_ip() de um objeto rect INSERE UM RETÂNGULO (rect2)
                # DENTRO DE OUTRO OBJETO RETÂNGULAR (rect1)
                #
                rect1.clamp_ip(rect2)

            if event.key == pygame.K_x:
                ##############################################
                # o método: clip() de um objeto rect PEGA O OBJETO RECT INSERIDO DENTRO
                # DE OUTRO OBJETO RECT (pega o: rect2 QUE ESTÁ DENTRO DE: rect1), E
                # RETORNA ESSE OBJETO (rect2).
                #
                rect3 = rect1.clip(rect2)
                rect3.x = 280 # inserindo o objeto retornado (rect2) em uma nova posição em: x
                rect3.y = 120 # inserindo o objeto retornado (rect2) em uma nova posição em: y
                print(rect3)
                active2 = True



    #########################################
    # Desenhando as SUPERFÍCIES que GERAMOS UMA ÁREA RETÂNGULAR, na tela do Pygame...
    #
    screen.blit(surf2, (rect_surf2.x, rect_surf2.y))
    screen.blit(surf1, (rect_surf1.x, rect_surf1.y))
    if active1:
        screen.blit(surf3, (rect_surf3.x, rect_surf3.y)) # DESENHA A SUPERFÍCIE AMARELA (YELLOW)

    ########################################
    # Desenhando os objetos RECT na tela do Pygame...
    #
    pygame.draw.rect(screen, GREEN, rect2)
    pygame.draw.rect(screen, RED, rect1)
    if active2:
        pygame.draw.rect(screen, YELLOW, rect3)


    pygame.display.update()
    clock.tick(FPS)

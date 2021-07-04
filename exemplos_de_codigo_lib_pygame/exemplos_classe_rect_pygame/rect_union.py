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

######################################
# rects do primeiro Exemplo: lado esquerdo
#
rect1 = pygame.Rect(20, 20, 30, 30)
rect2 = pygame.Rect(100, 90, 50, 50)
active1 = False

######################################
# rects do segundo Exemplo: lado direito
#
rect4 = pygame.Rect(200, 20, 30, 30)
rect5 = pygame.Rect(300, 20, 30, 30)
active2 = False


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                ######################################
                # Acionando o primeiro Exemplo: lado esquerdo
                ######################################
                # O método: union() de um objeto rect, UNI AS ÁREAS RETÂNGULARES
                # DOS DOIS RECTS COBRINDO TODA A ÁREA RETÂNGULAR (DENTRO E FORA) ENTRE ESSES DOIS OBJETOS
                # RETORNANDO ESSA NOVA ÁREA COBERTA.
                #
                rect3 = rect1.union(rect2)
                active1 = True

            if event.key == pygame.K_d:
                ######################################
                # Acionando o segundo Exemplo: lado direito
                ######################################
                # O método: union() de um objeto rect, UNI AS ÁREAS RETÂNGULARES
                # DOS DOIS RECTS COBRINDO TODA A ÁREA RETÂNGULAR (DENTRO E FORA) ENTRE ESSES DOIS OBJETOS.
                # RETORNANDO ESSA NOVA ÁREA COBERTA.
                #
                rect6 = rect4.union(rect5)
                active2 = True

    #########################################
    # Primeiro exemplo: OS DOIS QUADRADOS DO LADO ESQUERDO DA TELA
    #
    pygame.draw.rect(screen, RED, rect1)
    pygame.draw.rect(screen, BLUE, rect2)

    if active1:
        pygame.draw.rect(screen, YELLOW, rect3) # MOSTRA A ÁREA COBERTA EM AMARELO (YELLOW)

    #########################################
    # Segundo exemplo: OS DOIS QUADRADOS DO LADO DIREITO DA TELA
    #
    pygame.draw.rect(screen, RED, rect4)
    pygame.draw.rect(screen, BLUE, rect5)

    if active2:
        pygame.draw.rect(screen, YELLOW, rect6) # MOSTRA A ÁREA COBERTA EM AMARELO (YELLOW)

    pygame.display.update()
    clock.tick(FPS)

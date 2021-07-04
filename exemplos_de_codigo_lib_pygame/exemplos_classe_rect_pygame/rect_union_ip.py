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

######################################
# rects do segundo Exemplo: lado direito
#
rect4 = pygame.Rect(200, 20, 30, 30)
rect5 = pygame.Rect(300, 20, 30, 30)


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
                # O método: union_ip() de um objeto rect, UNI AS ÁREAS RETÂNGULARES
                # DOS DOIS RECTS COBRINDO TODA A ÁREA RETÂNGULAR (DENTRO E FORA) ENTRE ESSES DOIS OBJETOS.
                #
                rect1.union_ip(rect2)

            if event.key == pygame.K_d:
                ######################################
                # Acionando o segundo Exemplo: lado direito
                ######################################
                # O método: union_ip() de um objeto rect, UNI AS ÁREAS RETÂNGULARES
                # DOS DOIS RECTS COBRINDO TODA A ÁREA RETÂNGULAR (DENTRO E FORA) ENTRE ESSES DOIS OBJETOS.
                #
                rect4.union_ip(rect5)

    #########################################
    # Primeiro exemplo: OS DOIS QUADRADOS DO LADO ESQUERDO DA TELA
    #
    pygame.draw.rect(screen, RED, rect1)
    pygame.draw.rect(screen, BLUE, rect2)


    #########################################
    # Segundo exemplo: OS DOIS QUADRADOS DO LADO DIREITO DA TELA
    #
    pygame.draw.rect(screen, RED, rect4)
    pygame.draw.rect(screen, BLUE, rect5)


    pygame.display.update()
    clock.tick(FPS)

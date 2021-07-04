import pygame

RED = (200, 0, 0)
GREEN = (0, 200 , 0)
BLUE = (0, 0, 200)

WIDTH = 400
HEIGHT = 400
FPS = 60

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

rect = pygame.Rect(WIDTH/2, HEIGHT/2, 30, 30)
size = 10


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                ###################################
                # O método: inflate_ip() de um objeto rect INFLA O OBJETO RECT
                # EM CADA UM DOS LADOS DO RETÂNGULO Á UMA DETERMINADA DISTÂNCIA POR VEZ.
                # Essa distância É INFLADA DE ACORDO COM O VALOR INSERIDO NO EIXO (x, y).
                # Como a variável: size está configurada com o valor: 10, o
                # nosso objeto rect INFLARÁ 10 PIXELS EM CADA UMA DAS 4 DIREÇOES (LADOS DO RECT)
                # se apertarmos a tecla: w.
                #
                # É por isso que a documentação diz que o objeto rect é
                # operado a partir do local onde ele está, pq o objeto rect
                # INFLA EXATAMENTE Á UMA DETERMINADA QUANTIDADE DE PIXELS A
                # PARTIR DA POSIÇÃO ATUAL EM QUE O OBJETO ESTÁ NA TELA.
                rect.inflate_ip(size, size)



    ##############################################
    # Desenha o rect 
    pygame.draw.rect(screen, GREEN, rect)


    pygame.display.update()
    clock.tick(FPS)

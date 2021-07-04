import pygame

RED = (200, 0, 0)
GREEN = (0, 200 , 0)
BLUE = (0, 0, 200)
BLACK = (0, 0, 0)

FPS = 60

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

rect = pygame.Rect(90, 80, 30, 30)
speed = 35


running = True
while running:

    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                ###################################3
                # O método: move_ip() de um objeto rect MOVE O OBJETO RECT
                # Á UMA DETERMINADA DISTÂNCIA POR VEZ. Essa distância
                # é percorrida de acordo com o valor inserido no eixo (x, y).
                # Como a variável: speed está configurada com o valor: 35, o
                # nosso objeto rect percorrerá 35 pixels em qualquer
                # direção apertando as teclas: a, w, s, d.
                #
                # É por isso que a documentação diz que o objeto rect é
                # operado a partir do local onde ele está, pq o objeto rect
                # SE MOVE EXATAMENTE Á UMA DETERMINADA QUANTIDADE DE PIXELS A
                # PARTIR DA POSIÇÃO ATUAL EM QUE O OBJETO ESTÁ NA TELA.
                rect.move_ip(-speed, 0)

            if event.key == pygame.K_d:
                rect.move_ip(speed, 0)

            if event.key == pygame.K_w:
                rect.move_ip(0, -speed)

            if event.key == pygame.K_s:
                rect.move_ip(0, speed)


    pygame.draw.rect(screen, RED, rect)

    pygame.display.update()
    clock.tick(FPS)

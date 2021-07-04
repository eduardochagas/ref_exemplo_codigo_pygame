import pygame

RED = (200, 0, 0)
GREEN = (0, 200 , 0)
BLUE = (0, 0, 200)
BLACK = (0, 0, 0)

FPS = 60

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

#######################################
# Primeiro Rect criado (rect Verde)
#
rect = pygame.Rect(60, 30, 30, 30)
#########################################
# Segundo Rect criado (rect Azul)
#
rect2 = pygame.Rect(90, 120, 30, 30)
velx = 0 # variável para a velocidade no eixo x do rect Azul
vely = 0 # variável para a velocidade no eixo y do rect Azul
speed = 5 # variável que insere o valor de movimento nos eixos (x,y) do rect Azul.

running = True
while running:

    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           exit()

        if event.type == pygame.KEYDOWN:
            ##########################################
            # Aqui, as teclas: a,w,d,s movem o rect Verde...
            #
            if event.key == pygame.K_a:
            ######################################
            # O método: move() de um objeto rect retorna O PROPRIO OBJETO RECT
            # em um nova posição (x,y) na tela.
            #
                rect = rect.move(-35, 0)
            if event.key == pygame.K_d:
                rect = rect.move(105, 0)

            if event.key == pygame.K_w:
                rect = rect.move(0, -105)

            if event.key == pygame.K_s:
                rect = rect.move(0, 85)

            ########################################
            #  Aqui, as teclas de seta: left, right, up, down,
            #  movem o rect azul na tela do pygame.
            #
            if event.key == pygame.K_LEFT:
                velx += -speed
            if event.key == pygame.K_RIGHT:
                velx += speed
            if event.key == pygame.K_UP:
                vely += -speed
            if event.key == pygame.K_DOWN:
                vely += speed

    ###########################################
    # Desenhando o rect Verde (primeiro rect criado)
    #
    pygame.draw.rect(screen, GREEN, rect)

    ###########################################
    # Desenhando o rect Azul(segundo rect criado)
    #   OBS: nessa linha, o método: rect2.move() está funcionando pq
    #   rect2.move() RETORNA O PRÓPRIO OBJETO RECT, SÓ QUE EM UMA NOVA POSIÇÃO
    pygame.draw.rect(screen, BLUE, rect2.move(velx, vely))


    pygame.display.update()
    clock.tick(FPS)

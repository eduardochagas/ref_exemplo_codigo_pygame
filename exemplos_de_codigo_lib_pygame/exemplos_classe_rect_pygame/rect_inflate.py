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
size = 100


rect2 = pygame.Rect(200, 80, 30, 30)
x = 0
y = 0

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                ##########################################
                # O método: inflate() de um objeto rect RETORNA O PROPRIO OBJETO,
                # SÓ QUE EM UMA NOVA POSIÇÃO NA TELA do pygame.
                rect = rect.inflate(size, size)

            if event.key == pygame.K_s:
                x += 150
                y += 150

    ##############################################
    # Desenha o primeiro rect (Verde)
    pygame.draw.rect(screen, GREEN, rect)


    ##############################################
    # Desenha o segundo rect (Vermelho)
    #   OBS: nessa linha, o método: rect2.inflate() está funcionando pq
    #   rect2.inflate() RETORNA O PRÓPRIO OBJETO RECT, SÓ QUE EM UMA NOVA POSIÇÃO.
    pygame.draw.rect(screen, RED, rect2.inflate(x, y))

    pygame.display.update()
    clock.tick(FPS)

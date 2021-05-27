import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

pygame.init()

screen = pygame.display.set_mode((640, 480),0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert()

# Nosso objeto clock
clock = pygame.time.Clock()

x1 = 0
x2 = 0

# A velocidade
speed = 250

frame_no = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x1, 50))
    screen.blit(sprite, (x2, 250))

    time_passed = clock.tick(30) # quando não inserimos um valor no parâmetro, retorna um valor em milisegundos
    time_passed_seconds = time_passed / 1000.0 # converte de milisegundos para segundos

    distance_moved = time_passed_seconds * speed
    x1 += distance_moved

    if (frame_no % 5) == 0:
        distance_moved = time_passed_seconds * speed
        x2 += distance_moved * 5

    # Se a imagem ultrapassar a extremidade da tela, mova-a de volta
    if x1 > 640:
        x1 -= 640
    if x2 > 640:
        x2 -=640

    pygame.display.update()
    frame_no += 1




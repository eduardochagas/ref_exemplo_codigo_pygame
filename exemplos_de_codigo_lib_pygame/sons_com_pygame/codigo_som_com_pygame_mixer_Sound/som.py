import pygame
import os

###########################################################
# definindo o camimho até a pasta de som do programa
#   OBS: é obrigatório inserir o caractere de barra no final
#   do nome da pasta, caso contrário dará erro !!!
#
path = os.path.join(os.path.dirname(__file__), 'sound/')
############################################################
# definindo o caminho da pasta de som, até o arquivo de som: Soco.ogg !!!
#
sound_soco = os.path.join(os.path.dirname(path), 'Soco.ogg')
############################################################
# definindo o caminho da pasta de som, até o arquivo de som: win_sound.wav !!!
sound_winner = os.path.join(os.path.dirname(path), 'win_sound.wav')
############################################################
# definindo o caminho da pasta de som, até o arquivo de som: motoserra.mp3 !!!
sound_chainsaw = os.path.join(os.path.dirname(path), 'motoserra.ogg')


############################################
#  Iniciando o Pygame.....
# 
pygame.init()

screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

FPS = 60

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                ##############################################
                # Inserindo o nosso arquivo de som (sound_chainsaw) dentro da classe: pygame.mixer.Sound() do pygame !!!
                #
                #   OBS: LEMBRANDO QUE, A CLASSE: pygame.mixer.Sound() NÃO ACEITA ARQUIVOS: .mp3, ACEITA SOMENTE 
                #   ARQUIVOS: .ogg E .wav.
                #
                sound_chainsaw = pygame.mixer.Sound(sound_chainsaw)
                ######################################################
                #
                # Usando o método: set_volume() da classe: pygame.mixer.Sound() para configurarmos
                # o volume do som inserido na classe: pygame.mixer.Sound() !!!!!
                #  
                #   o valor a ser passado tem que ser um valor entre: 0.0 e 1.0, onde:
                #
                #     0.0 - não sai som nenhum
                #     1.0 - valor mais alto possível no pygame !!!
                #
                #     OBS: SE VC INSERIR NO PARÂMETRO MÉTODO: set_volume() UM VALOR MAIOR DO QUE: 1.0,
                #     O VALOR DO VOLUME SERÁ CONFIGURADO PARA: 1.0
                #
                sound_chainsaw.set_volume(0.3)
                ############################################
                # o método: play() da classe: pygame.mixer.Sound(), possui 3 parâmetros:
                #
                #   loops - o primeiro parâmetro (loops) define a QUANTIDADE DE LOOPS que 
                #   o som vai executar
                #
                #   maxtime - o segundo parâmetro (maxtime) é usado para PARAR DE TOCAR O SOM EM ATÉ 
                #   UM DETERMINADO MILISEGUNDOS do som tocado.
                #
                #   fade_ms - o terceiro parâmetro (fade_ms) é usado para FAZER O SOM COMEÇAR A
                #   TOCAR NO VOLUME 0 e ir SUBINDO O SOM ATÉ O VOLUME TOTAL DO SOM.
                # 
                #     OBS: O SOM INSERIDO NA CLASSE: pygame.mixer.Sound() PODE ACABAR ANTES 
                #     DO FADE-IN SER COMPLETADO !!! 
                #     -------------------------------------------------------------------------------
                #     OBS2: TENTEI FAZER FUNCIONAR O PARÂMETRO: fade_ms, MAS SINCERAMENTE, 
                #     NÃO CONSEGUI DE JEITO NENHUM, NA DÚVIDA, NÃO USE-O, ATÉ PQ 
                #     O VALOR PADRÃO DELE É ZERO, ENTÃO, NÃO HÁ O QUE SE PREOCUPAR !!!
                #     --------------------------------------------------------------------------------
                #
                #  OBS: como o parâmetro: maxtime está com o valor: 5000 (significa: 5000 milisegundos), o som da serra elétrica
                #  tocará somente 5 segundos (pq 5000 milisegundos é o mesmo que 5 segundos !!!).
                #
                sound_chainsaw.play(loops=0, maxtime=5000, fade_ms=0)
                ######################################################
                # método: get_length() da classe: pygame.mixer.Sound(), mostrando o tamanho do arquivo do som (sound_chainsaw) !!!
                #
                print('Por curiosidade, o tamanho do audio da motoserra é: {}'.format(sound_chainsaw.get_length()))

            ########################################################################################
            #  Esses dois exemplos abaixo, faz o mesmo que o exemplo explicado logo acima. São só 
            #  mais exemplos para vc entender e ter como referência !!!!!!!
            #
            if event.key == pygame.K_a:
                soco = pygame.mixer.Sound(sound_soco)
                soco.play(0, 0, 100)
                print('Por curiosidade, o tamanho do audio do soco é: {}'.format(soco.get_length()))

            if event.key == pygame.K_d:
               som_de_vitoria = pygame.mixer.Sound(sound_winner)
               som_de_vitoria.play(0, 0, 200)
               print('O tamanho do audio do som de vitória é: {}'.format(som_de_vitoria.get_length()))


    clock.tick(FPS)
    pygame.display.update()



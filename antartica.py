# Código para imagens de conscientização para o aquecimento global
import pygame
import os
from assets import * 
from config import FPS, WIDTH, HEIGHT, GAME, QUIT, END, ANTARTICA


def antartica_screen(window):
    assets = load_assets()

    #Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    lista_imagens = []

    imagem1 = assets[GLOBAL_WARMING_1]
    imagem1 = pygame.transform.scale(imagem1, (WIDTH - 100, HEIGHT - 100))
    imagem1_rect = imagem1.get_rect()
    lista_imagens.append(imagem1)

    imagem2 = assets[GLOBAL_WARMING_2]
    imagem2 = pygame.transform.scale(imagem2, (WIDTH - 100, HEIGHT - 100))
    imagem2_rect = imagem2.get_rect()
    lista_imagens.append(imagem2)

    imagem3 = assets[GLOBAL_WARMING_3]
    imagem3 = pygame.transform.scale(imagem3, (WIDTH - 100, HEIGHT - 100))
    imagem3_rect = imagem3.get_rect()
    lista_imagens.append(imagem3)

    imagem4 = assets[GLOBAL_WARMING_4]
    imagem4 = pygame.transform.scale(imagem4, (WIDTH - 100, HEIGHT - 100))
    imagem4_rect = imagem4.get_rect()
    lista_imagens.append(imagem4)

    imagem5 = assets[GLOBAL_WARMING_5]
    imagem5 = pygame.transform.scale(imagem5, (WIDTH - 100, HEIGHT - 100))
    imagem5_rect = imagem5.get_rect()
    lista_imagens.append(imagem5)

    imagem6 = assets[GLOBAL_WARMING_6]
    imagem6 = pygame.transform.scale(imagem6, (WIDTH - 100, HEIGHT - 100))
    imagem6_rect = imagem6.get_rect()
    lista_imagens.append(imagem6)

    texto1 = 'O aquecimento global está comprometendo a vida de muitos animais que vivem no gelo'

    texto2 = 'Faça a sua parte, colabore com o meio ambiente e evite que mais pinguins morram de fome'

    running = True

    tempo_inicial = pygame.time.get_ticks()

    tempo_de_troca = 4166  #ms

    x = 1
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

        window.blit(imagem1, imagem1_rect)

        now = pygame.time.get_ticks()
        elapsed_ticks = now - tempo_inicial

        if elapsed_ticks > tempo_de_troca:
            window.blit(imagem'{}'.format(lista_imagens[x]), imagem'{}'.format(lista_imagens[x])_rect)
            x += 1
            tempo_inicial = pygame.time.get_ticks()

        if x == 6:
            state = END
            running = False

        texto1_surface = assets['antartica_font'].render(texto1, True, BLACK)
        texto1_rect = texto2_surface.get_rect()
        texto1_rect.midtop = (WIDTH / 2, 30)
        window.blit(texto1_surface, texto2_rect)

        texto2_surface = assets['antartica_font'].render(texto2, True, BLACK)
        texto2_rect = texto2_surface.get_rect()
        texto2_rect.midtop = (WIDTH / 2, 520)
        window.blit(texto2_surface, texto2_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state
# Código para imagens de conscientização para o aquecimento global
import pygame
import os
from assets import * 
from config import FPS, WIDTH, HEIGHT, QUIT, END, ANTARTIDA, RED

 
def antartida_screen(window):
    assets = load_assets()

    #Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    lista_imagens = []

    imagem1 = assets[GLOBAL_WARMING_1]
    imagem1 = pygame.transform.scale(imagem1, (WIDTH, HEIGHT))
    imagem_rect = imagem1.get_rect()
    lista_imagens.append(imagem1)

    imagem2 = assets[GLOBAL_WARMING_2]
    imagem2 = pygame.transform.scale(imagem2, (WIDTH, HEIGHT))
    lista_imagens.append(imagem2)

    imagem3 = assets[GLOBAL_WARMING_3]
    imagem3 = pygame.transform.scale(imagem3, (WIDTH, HEIGHT))
    lista_imagens.append(imagem3)

    imagem4 = assets[GLOBAL_WARMING_4]
    imagem4 = pygame.transform.scale(imagem4, (WIDTH, HEIGHT))
    lista_imagens.append(imagem3)

    texto1 = 'O aquecimento global esta comprometendo'

    texto2 =  'a vida de muitos animais que vivem no gelo'

    texto3 = 'Contribua com a sua parte, colabore com o meio ambiente'

    texto4 = 'e evite que mais pinguins morram de fome'

    running = True

    tempo_inicial = pygame.time.get_ticks()

    tempo_de_troca = 4166  #ms

    x = 1
    fundo = imagem1
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

        now = pygame.time.get_ticks()
        elapsed_ticks = now - tempo_inicial

        if elapsed_ticks > tempo_de_troca:

            if x == 4:
                state = END
                running = False

            else:
                fundo = lista_imagens[x]
            
            x += 1
            tempo_inicial = pygame.time.get_ticks()

        window.blit(fundo, imagem_rect)
        texto1_surface = assets['antartida_font'].render(texto1, True, RED)
        texto1_rect = texto1_surface.get_rect()
        texto1_rect.midtop = (WIDTH / 2, 30)
        window.blit(texto1_surface, texto1_rect)

        texto2_surface = assets['antartida_font'].render(texto2, True, RED)
        texto2_rect = texto2_surface.get_rect()
        texto2_rect.midtop = (WIDTH / 2, 70)
        window.blit(texto2_surface, texto2_rect)

        texto3_surface = assets['antartida_font'].render(texto3, True, RED)
        texto3_rect = texto3_surface.get_rect()
        texto3_rect.midtop = (WIDTH / 2, 480)
        window.blit(texto3_surface, texto3_rect)

        texto4_surface = assets['antartida_font'].render(texto4, True, RED)
        texto4_rect = texto4_surface.get_rect()
        texto4_rect.midtop = (WIDTH / 2, 530)
        window.blit(texto4_surface, texto4_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state
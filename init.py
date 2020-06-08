#init
import pygame
import random
import os
from assets import *    
from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT, INSTRUCTIONS, END 
 
def init_screen(screen):
    assets = load_assets()

    # Título do jogo:
    titulo = assets[INIT_FONT].render('Pinguim Faminto', True, (0, 0, 0))
    titulo_rect = titulo.get_rect()
    titulo_rect.x = 50
    titulo_rect.y = 100

    # Botao para instrucoes:
    inst = assets[INIT_FONT_2].render('Aperte seta para baixo para ver as instruções de jogo', True, (0, 0, 0))
    inst_rect = inst.get_rect()
    inst_rect.x = 50
    inst_rect.y = 500
    
    # Botao para jogar:
    jogar = assets[INIT_FONT_3].render('Aperte espaco para jogar', True, (0, 0, 0))
    jogar_rect = jogar.get_rect()
    jogar_rect.x = 200
    jogar_rect.y = 400


    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    
    #Carrega o fundo da tela inicial
    background = assets[INIT_BACKGROUND]
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    running = True
    
    keys_down = {}

    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            
            # Verifica cliques do Mouse:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                
                # Verifica se jogador clicou em "Jogar":
                if x >= 200 and x <= 500 and y >=300 and y <= 400:
                    state = GAME

                # Verifica se jogador clicou em "Instruções":
                if x >= 200 and x <= 500 and y >=420 and y <= 500:
                    state = INSTRUCOES
                
                running = False
        
        screen.blit(background, background_rect)
        screen.blit(titulo, titulo_rect)
        screen.blit(inst, inst_rect)
        screen.blit(jogar, jogar_rect)

        #Atualiza o background
        pygame.display.flip()

    return state
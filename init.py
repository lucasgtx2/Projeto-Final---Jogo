#init
import pygame
import random
import os
from assets import *    
from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT, INSTRUCTIONS, END 
 
def init_screen(screen):
    assets = load_assets()

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
                    running = False

                # Verifica se jogador clicou em "Instruções":
                if x >= 200 and x <= 500 and y >=420 and y <= 500:
                    state = INSTRUCTIONS
                    running = False
        
        screen.blit(background, background_rect)

        #Atualiza o background
        pygame.display.flip()

    return state
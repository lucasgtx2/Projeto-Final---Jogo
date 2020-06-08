#código para instruções
import pygame
import os
from assets import * 
from config import FPS, WIDTH, HEIGHT, INIT, QUIT 
 
def instrucoes_screen(screen):
    assets = load_assets()

    background = assets[INSTRUCOES]
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
                
                # Verifica se jogador clicou em "Voltar":
                if x >= 550 and x <= 650 and y >= 450 and y <= 550:
                    state = INIT
                    running = False
        
        screen.blit(background, background_rect)

    return state
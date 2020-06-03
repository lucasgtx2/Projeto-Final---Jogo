#código para instruções
import pygame
import os
from assets import * 

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

            # Passa para o jogo quando o jogador apertar "espaço"
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
            
                if event.key == pygame.K_SPACE:
                    keys_down[event.key] = True
                    state = GAME
                    running = False
                    
                if event.key == pygame.K_DOWN:
                    keys_down[event.key] = True
                    state = INIT
                    running = False
        
        screen.blit(background, background_rect)

    return state
#tela final, apos perder. 
import pygame 
import random
import os
from assets import *    
from config import IMG_DIR, BLACK, FPS, QUIT, WIDTH, HEIGHT, INSTRUCTIONS, INIT, GAME
from pinguim_game_screen import * 
 
def end_screen(window, score):
    assets = load_assets()

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    game_over = assets[END_IMG]
    game_over = pygame.transform.scale(game_over, (WIDTH, HEIGHT))
    game_over_rect = game_over.get_rect()

    # Aparece pontuacao:
    pontuacao = assets[SCORE_FONT_END].render('{}'.format(score), True, YELLOW)
    pontuacao_rect = pontuacao.get_rect()
    pontuacao_rect.x = WIDTH/2 - 120
    pontuacao_rect.y = 165
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
                
                # Verifica se jogador clicou em "Jogar de novo":
                if x >= 200 and x <= 500 and y >=300 and y <= 400:
                    state = INIT
                
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

        window.blit(game_over, game_over_rect)
        window.blit(pontuacao, pontuacao_rect)
        pygame.display.update()  # Mostra o novo frame para o jogador
    
    return state  
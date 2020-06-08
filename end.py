#tela final, apos perder. 
import pygame
import random
import os
from assets import *    
from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT, INSTRUCTIONS
from pinguim_game_screen import score
  
def end_screen(screen):
    assets = load_assets()

    background = assets[END]
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    # Botao para jogar:
    jogar = assets[INIT_FONT_3].render('Aperte espaco para jogar novamente', True, (0, 0, 0))
    jogar_rect = jogar.get_rect()
    jogar_rect.x = 50
    jogar_rect.y = 400

    # Aparece pontuacao:
    pontuacao = assets[INIT_FONT_4].render('Score: {}'.format(score), True, (255, 0, 0))
    pontuacao_rect = pontuacao.get_rect()
    pontuacao_rect.x = 50
    pontuacao_rect.y = 400

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

        screen.blit(jogar, jogar_rect)
        screen.blit(pontuacao, pontuacao_rect)
    
    return state
#init
import pygame
import random
from os import path

from config import IMG_DIR, BLACK, FPS, GAME, QUIT 
from assets import assets[BACKGROUND]

def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()


    ''' Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, assets[BACKGROUND])).convert()
    background_rect = background.get_rect()'''
    
    running = True

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
                    state = GAME
                    return state
        
        screen.fill(BLACK)

    return state
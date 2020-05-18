#init
import pygame
import random
import os

from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT 
from assets import load_assets

def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()


    #Carrega o fundo da tela inicial
    '''background = assets['init_background_img']
    background_rect = background.get_rect()'''
    background = pygame.image.load(os.path.join(IMG_DIR, 'init background.jpg')).convert_alpha()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

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
                    keys_down[event.key] = True
                    state = GAME
                    running = False
        
        screen.blit(background, background_rect)

    return state
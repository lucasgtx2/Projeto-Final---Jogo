# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import os
from config import WIDTH, HEIGHT, INIT, GAME, QUIT, END, INSTRUCTIONS
from init import init_screen
from pinguim_game_screen import game_screen
from codigo_para_os_sprites import *
from assets import *
from end import end_screen
from instrucoes import instrucoes_screen

pygame.init() 
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pinguim Faminto')

# loop principal do jogo:
state = INIT
assets = load_assets()

while state != QUIT:

    if state == INIT:
        pygame.mixer.music.stop()
        musica = pygame.mixer.music.load(os.path.join(SND_DIR, 'musica-tela-inicial.wav'))

        #musica = pygame.mixer.music.load(os.path.join(SND_DIR, 'violao-inicio.wav'))

        pygame.mixer.music.play()

        state = init_screen(window)

    elif state == INSTRUCTIONS:
        pygame.mixer.music.stop()
        musica = pygame.mixer.music.load(os.path.join(SND_DIR, 'musica-tela-inicial.wav'))
        pygame.mixer.music.play()
        
        state = instrucoes_screen(window)

    elif state == GAME:
        pygame.mixer.music.stop()
        musica = pygame.mixer.music.load(os.path.join(SND_DIR, 'musica-de-fundo.wav'))
        pygame.mixer.music.play()

        state, score = game_screen(window)

    elif state == END:
        assets[PINGUIM_MORREU_SND].play()
        pygame.mixer.music.stop()
        musica = pygame.mixer.music.load(os.path.join(SND_DIR, 'vento.wav'))

        #musica = pygame.mixer.music.load(os.path.join(SND_DIR, 'violao-antartica.wav'))

        pygame.mixer.music.play()
        
        state = end_screen(window, score)

    else:
        state = QUIT

# ===== Finalização =====  
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados   
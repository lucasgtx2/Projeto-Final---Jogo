# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import os
from config import WIDTH, HEIGHT, INIT, GAME, QUIT, END, INSTRUCTIONS, ANTARTIDA
from init import init_screen
from game_screen import game_screen
from codigo_para_os_sprites import *
from assets import *
from end import end_screen
from instrucoes import instrucoes_screen
from antartida import antartida_screen
  
pygame.init() 
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pinguim Faminto')

# loop principal do jogo:
state = INIT
assets = load_assets()

i = 0
while state != QUIT:
    if state == INIT:
        pygame.mixer.music.stop()
        musica = pygame.mixer.music.load(os.path.join(SND_DIR, 'violao-inicio.wav'))
        pygame.mixer.music.set_volume(2)

        pygame.mixer.music.play(-1)

        state = init_screen(window)

    elif state == INSTRUCTIONS:
        pygame.mixer.music.stop()
        musica = pygame.mixer.music.load(os.path.join(SND_DIR, 'violao-inicio.wav'))
        pygame.mixer.music.set_volume(2)
        pygame.mixer.music.play(-1)
        
        state = instrucoes_screen(window)

    elif state == GAME:
        pygame.mixer.music.stop()
        musica = pygame.mixer.music.load(os.path.join(SND_DIR, 'musica-de-fundo.wav'))
        pygame.mixer.music.play(-1)

        state, score = game_screen(window)
    
    elif state == ANTARTIDA and i==0:
        pygame.mixer.music.stop()
        musica = pygame.mixer.music.load(os.path.join(SND_DIR, 'violao-antartica.wav'))
        pygame.mixer.music.play()

        state = antartida_screen(window)

    elif state == END or state == ANTARTIDA:
        if i != 0:
            pygame.mixer.music.stop()
            musica = pygame.mixer.music.load(os.path.join(SND_DIR, 'vento.wav'))

            pygame.mixer.music.play()
            state = end_screen(window, score)

        i += 1

    else:
        state = QUIT

# ===== Finalização =====  
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
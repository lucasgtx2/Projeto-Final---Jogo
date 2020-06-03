# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import os
from config import WIDTH, HEIGHT, INIT, GAME, QUIT, END
from init import init_screen
from pinguim_game_screen import game_screen
from codigo_para_os_sprites import *
#from end import end

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
        assets[MUSICA_INICIAL_SND].play()
        state = init_screen(window)
    elif state == GAME:
        assets[MUSICA_INICIAL_SND].stop()
        assets[MUSICA_JOGO_SND].play()
        state = game_screen(window)
    elif state == END:
        assets[MUSICA_JOGO_SND].stop()
        state = end_screen(window)
    else:
        state = QUIT

# ===== Finalização =====  
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
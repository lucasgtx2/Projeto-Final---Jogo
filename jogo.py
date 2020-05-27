# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import os
from config import WIDTH, HEIGHT, INIT, GAME, QUIT, END
from init import init_screen
#from game screen import game screen
#from end import end
    
pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pinguim Faminto')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    elif state == END:
        state = end_screen(window)
    else:
        state = QUIT
# ===== Finalização =====  
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados 
#game screen
import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, END, QUIT
from assets import load_assets
from sprites import Pinguim

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()
 
    #Criando grupos com os sprites:
    all_sprites = pygame.sprite.Group()
    all_meat = pygame.sprite.Group()
    all_whole_salmon = pygame.sprite.Group()
    all_rocks = pygame.sprite.Groups()
    all_
    groups = {}
    groups['all_sprites'] = all_sprites
    

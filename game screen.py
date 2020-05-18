#game screen
import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, END, QUIT
from assets import load_assets
from código para os sprites import Pinguim, Carne, Salmao_inteiro, Pedra, Bomba

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()
 
    #Criando grupos com os sprites:
    all_sprites = pygame.sprite.Group()
    all_carnes = pygame.sprite.Group()
    all_pedras = pygame.sprite.Groups()
    all_bombas = pygame.sprite.Groups()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_carnes'] = all_carnes
    groups['all_pedras'] = all_pedras
    groups['all_bombas'] = all_bombas

    # Criando o jogador
    player = Pinguim(groups, assets)
    all_sprites.add(player)
    # Criando as carnes (salmão)
    for i in range(6):
        carne = Carne(assets)
        all_sprites.add(carne)
        all_carnes.add(carne)

    #Criando salmão inteiro:
    salmao_inteiro = Salmao_inteiro(groups, assets)
    all_sprites.add(salmao_inteiro)

    #Criando pedras:
    for i in range(3):
        pedra = Pedra(groups, assets)
        all_pedras.add(pedra)
        all_sprites.add(pedra)

    #Criando bomba:
    bomba = Bomba(groups, assets)
    all_bombas.add(bomba)
    all_sprites.add(bomba)
    
    DONE = 0
    PLAYING = 1
    EXPLODING = 2
    state = PLAYING

    keys_down = {}
    score = 0
    lives = 3
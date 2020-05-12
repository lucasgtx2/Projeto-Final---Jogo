#codigo para definicao dos assets
import pygame
import os
from config import IMG_DIR, FNT_DIR, PINGUIMD_WIDTH, PINGUIMD_HEIGHT, PINGUIMP_WIDTH, PINGUIMP_HEIGHT, SALMAOC_WIDTH, SALMAOC_HEIGHT, SALMAOD_WIDTH, SALMAOD_HEIGHT, BOMBA_PEDRA_WIDTH, BOMBA_PEDRA_HEIGHT


BACKGROUND = 'background_img'
PINGUIMD_IMG = 'pinguim_deitado_img'
PINGUIMP_IMG = 'pinguim_em_pe_img'
SALMAOC_IMG = 'salmao_carne_img'
SALMAOD_IMG = 'salmao_desenho_img'
'''#ainda nao definimos o score
SCORE_FONT = 'score_font'
'''
BOMBA_IMG = 'bomba_img'
PEDRA_IMG = 'pedra_img'


def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'fundo neve igloo.jpg')).convert()
    assets[PINGUIMD_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'pinguim deitado.jpg')).convert_alpha()
    assets[PINGUIMD_IMG] = pygame.transform.scale(assets['pinguim_deitado_img'], (PINGUIMD_WIDTH, PINGUIMD_HEIGHT))
    assets[PINGUIMP_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'pinguim em pe.jpg')).convert_alpha()
    assets[PINGUIMP_IMG] = pygame.transform.scale(assets['pinguim_em_pe_img'], (PINGUIMP_WIDTH, PINGUIMP_HEIGHT))
    assets[SALMAOC_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'salmao carne.jpg')).convert_alpha()
    assets[SALMAOC_IMG] = pygame.transform.scale(assets['salmao_carne_img'], (SALMAOC_WIDTH, SALMAOC_HEIGHT))
    assets[SALMAOD_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'salmao desenho.jpg')).convert_alpha()
    assets[SALMAOD_IMG] = pygame.transform.scale(assets['salmao_desenho_img'], (SALMAOD_WIDTH, SALMAOD_HEIGHT))
    assets[BOMBA_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'bomba desenho.jpg')).convert_alpha()
    assets[BOMBA_IMG] = pygame.transform.scale(assets['bomba_img'], (SALMAOD_WIDTH, SALMAOD_HEIGHT))
    assets[PEDRA_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'pedra desenho.jpg')).convert_alpha()
    assets[PEDRA_IMG] = pygame.transform.scale(assets['pedra_img'], (SALMAOD_WIDTH, SALMAOD_HEIGHT))


    '''# Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SND_DIR, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    pygame.mixer.music.set_volume(0.4)
    assets[BOOM_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl3.wav'))'''
    
    return assets

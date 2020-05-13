#codigo para definicao dos assets
import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR, PINGUIMD_WIDTH, PINGUIMD_HEIGHT, \
    PINGUIMP_WIDTH, PINGUIMP_HEIGHT, SALMAOC_WIDTH, SALMAOC_HEIGHT, SALMAOD_WIDTH, \
        SALMAOD_HEIGHT, BOMBA_PEDRA_WIDTH, BOMBA_PEDRA_HEIGHT


BACKGROUND = 'background_img'
PINGUIMD_IMG = 'pinguim_deitado_img'
PINGUIMP_IMG = 'pinguim_em_pe_img'
SALMAOC_IMG = 'salmao_carne_img'
SALMAOD_IMG = 'salmao_desenho_img'

BOMBA_IMG = 'bomba_img'
PEDRA_IMG = 'pedra_img'
EXPLOSAO_SND = 'explosao_arcade_snd'
PEDRA_SND = 'pedra_snd'
VENTO_SND = 'vento_snd'
MUSICA_JOGO_SND = 'musica_do_jogo_snd'
MUSICA_INICIAL_SND = 'musica_inicial_snd'
PODER_SND = 'poder_snd'
MORDIDA_SND = 'mordida_snd'

'''#ainda nao definimos o score
SCORE_FONT = 'score_font'
'''


def load_assets():
    assets = {}
    
    #Carrega as imagens:
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
    
    #Carrega os sons:
    pygame.mixer.music.load(os.path.join(SND_DIR, 'explosao arcade.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets[EXPLOSAO_SND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'explosao arcade.wav'))

    pygame.mixer.music.load(os.path.join(SND_DIR, 'som pedra.flac'))
    pygame.mixer.music.set_volume(0.4)
    assets[PEDRA_SND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'som pedra.flac'))

    pygame.mixer.music.load(os.path.join(SND_DIR, 'vento.m4a'))
    pygame.mixer.music.set_volume(0.4)
    assets[VENTO_SND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'vento.m4a'))

    pygame.mixer.music.load(os.path.join(SND_DIR, 'musica de fundo.mp3'))
    pygame.mixer.music.set_volume(0.4)
    assets[MUSICA_JOGO_SND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'musica de fundo.mp3'))

    pygame.mixer.music.load(os.path.join(SND_DIR, 'musica tela inicial.mp3'))
    pygame.mixer.music.set_volume(0.4)
    assets[MUSICA_INICIAL_SND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'musica tela inicial.mp3'))

    pygame.mixer.music.load(os.path.join(SND_DIR, 'som do poder.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets[PODER_SND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'som do poder.wav'))
    
    pygame.mixer.music.load(os.path.join(SND_DIR, 'mordida som.mp3'))
    pygame.mixer.music.set_volume(0.4)
    assets[PODER_SND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'mordida som.mp3'))

    return assets

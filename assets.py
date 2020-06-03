# Código para definição dos assets
import pygame
import os 
from config import IMG_DIR, SND_DIR, FNT_DIR, PINGUIMD_WIDTH, PINGUIMD_HEIGHT, \
    PINGUIMP_WIDTH, PINGUIMP_HEIGHT, SALMAOC_WIDTH, SALMAOC_HEIGHT, SALMAOD_WIDTH, \
        SALMAOD_HEIGHT, BOMBA_PEDRA_WIDTH, BOMBA_PEDRA_HEIGHT, WIDTH, HEIGHT

# Define imagens do jogo:   
BACKGROUND = 'background_img'

INIT_BACKGROUND = 'init_background_img'

INSTRUCOES = 'instrucoes_img'

END = 'end_img'

PINGUIMD_IMG = 'pinguim_deitado_img'
PINGUIMD_FLIP_IMG = 'pinguim_deitado_flip_img'

PINGUIMP_IMG = 'pinguim_em_pe_img'
PINGUIMP_FLIP_IMG = 'pinguim_em_pe_flip_img'

SALMAOC_IMG = 'salmao_carne_img'
SALMAOD_IMG = 'salmao_desenho_img'

PINGUIMPD_IMG = 'pinguim_poderoso_deitado_img'
PINGUIMPD_FLIP_IMG = 'pinguim_poderoso_deitado_flip_img'

PINGUIMPP_IMG = 'pinguim_poderoso_em_pe_img'
PINGUIMPP_FLIP_IMG = 'pinguim_poderoso_em_pe_flip_img'

PINGUIMGORDOP_IMG = 'pinguim_gordo_em_pe_img'
PINGUIMGORDOP_FLIP_IMG = 'pinguim_gordo_em_pe_flip_img'

PINGUIMGORDOD_IMG = 'pinguim_gordo_deitado_img'
PINGUIMGORDOD_FLIP_IMG = 'pinguim_gordo_deitado_flip_img'

BOMBA_IMG = 'bomba_img'
PEDRA_IMG = 'pedra_img'

# Define sons do jogo:
EXPLOSAO_SND = 'explosao_arcade_snd'
PEDRA_SND = 'pedra_snd'
VENTO_SND = 'vento_snd'
MUSICA_JOGO_SND = 'musica_do_jogo_snd'
MUSICA_INICIAL_SND = 'musica_inicial_snd'
PODER_SND = 'poder_snd'
MORDIDA_SND = 'mordida_snd'

# Define fontes do jogo:
SCORE_FONT = 'score_font'
INIT_FONT = 'init_font'
INIT_FONT_2 = 'init_font_2'
INIT_FONT_3 = 'init_font_3'
INIT_FONT_4 = 'init_font_4'


# Função principal que carrega os assets:
def load_assets():
    assets = {}
    
    #Carrega as imagens utilizadas:
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'fundo neve igloo.jpg')).convert()
    assets[BACKGROUND] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))

    assets[INIT_BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'init background.jpg')).convert()

    assets[PINGUIMD_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'pinguim deitado.jpg')).convert_alpha()
    assets[PINGUIMD_IMG] = pygame.transform.scale(assets['pinguim_deitado_img'], (PINGUIMD_WIDTH, PINGUIMD_HEIGHT))
    assets[PINGUIMD_FLIP_IMG] = pygame.transform.flip(assets['pinguim_deitado_img'], True, False)

    assets[PINGUIMP_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'pinguim em pe.png')).convert_alpha()
    assets[PINGUIMP_IMG] = pygame.transform.scale(assets['pinguim_em_pe_img'], (PINGUIMP_WIDTH, PINGUIMP_HEIGHT))
    assets[PINGUIMP_FLIP_IMG] = pygame.transform.flip(assets['pinguim_em_pe_img'], True, False)

    assets[PINGUIMPP_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'pinguim poderoso em pe.jpg')).convert_alpha()
    assets[PINGUIMPP_IMG] = pygame.transform.scale(assets['pinguim_poderoso_em_pe_img'], (PINGUIMP_WIDTH, PINGUIMP_HEIGHT))
    assets[PINGUIMPP_FLIP_IMG] = pygame.transform.flip(assets['pinguim_poderoso_em_pe_img'], True, False)

    assets[PINGUIMPD_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'pinguim poderoso deitado.jpg')).convert_alpha()
    assets[PINGUIMPD_IMG] = pygame.transform.scale(assets['pinguim_poderoso_deitado_img'], (PINGUIMP_WIDTH, PINGUIMP_HEIGHT))
    assets[PINGUIMPD_FLIP_IMG] = pygame.transform.flip(assets['pinguim_deitado_img'], True, False)

    '''assets[PINGUIMGORDOP_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'pinguim gordo em pe.jpg')).convert_alpha()
    assets[PINGUIMGORDOP_IMG] = pygame.transform.scale(assets['pinguim_gordo_em_pe_img'], (PINGUIMP_WIDTH, PINGUIMP_HEIGHT))
    assets[PINGUIMGORDOP_FLIP_IMG] = pygame.transform.flip(assets['pinguim_gordo_em_pe_img'], False, True)
    ''' '''
    assets[PINGUIMGORDOD_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'pinguim gordo deitado.jpg')).convert_alpha()
    assets[PINGUIMGORDOD_IMG] = pygame.transform.scale(assets['pinguim_gordo_deitado_img'], (PINGUIMP_WIDTH, PINGUIMP_HEIGHT))
    assets[PINGUIMGORDOD_FLIP_IMG] = pygame.transform.flip(assets['pinguim_gordo_deitado_img'], False, True)
    '''
    assets[SALMAOC_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'salmao carne.jpg')).convert_alpha()
    assets[SALMAOC_IMG] = pygame.transform.scale(assets['salmao_carne_img'], (SALMAOC_WIDTH, SALMAOC_HEIGHT))

    assets[SALMAOD_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'salmao desenho.jpg')).convert_alpha()
    assets[SALMAOD_IMG] = pygame.transform.scale(assets['salmao_desenho_img'], (SALMAOD_WIDTH, SALMAOD_HEIGHT))

    assets[BOMBA_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'bomba desenho.jpg')).convert_alpha()
    assets[BOMBA_IMG] = pygame.transform.scale(assets['bomba_img'], (SALMAOD_WIDTH, SALMAOD_HEIGHT))

    assets[PEDRA_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'pedra desenho.jpg')).convert_alpha()
    assets[PEDRA_IMG] = pygame.transform.scale(assets['pedra_img'], (SALMAOD_WIDTH, SALMAOD_HEIGHT))
    
    #Carrega os sons:
    pygame.mixer.music.load(os.path.join(SND_DIR, 'explosao-arcade.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets[EXPLOSAO_SND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'explosao-arcade.wav'))

    pygame.mixer.music.load(os.path.join(SND_DIR, 'som-pedra.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets[PEDRA_SND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'som-pedra.wav'))

    pygame.mixer.music.load(os.path.join(SND_DIR, 'vento.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets[VENTO_SND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'vento.wav'))

    pygame.mixer.music.load(os.path.join(SND_DIR, 'musica-de-fundo.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets[MUSICA_JOGO_SND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'musica-de-fundo.wav'))

    pygame.mixer.music.load(os.path.join(SND_DIR, 'musica-tela-inicial.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets[MUSICA_INICIAL_SND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'musica-tela-inicial.wav'))

    pygame.mixer.music.load(os.path.join(SND_DIR, 'som-do-poder.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets[PODER_SND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'som-do-poder.wav'))
    
    pygame.mixer.music.load(os.path.join(SND_DIR, 'mordida-som.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets[MORDIDA_SND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'mordida-som.wav'))

    # Carrega as fontes:
    assets[INIT_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'fonte titulo.ttf'), 75)
    assets[INIT_FONT_2] = pygame.font.Font(os.path.join(FNT_DIR, 'fonte titulo.ttf'), 25)
    assets[INIT_FONT_3] = pygame.font.Font(os.path.join(FNT_DIR, 'fonte titulo.ttf'), 25)
    assets[INIT_FONT_4] = pygame.font.Font(os.path.join(FNT_DIR, 'fonte titulo.ttf'), 40)
    
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'score fonte.ttf'), 28)
    
    return assets
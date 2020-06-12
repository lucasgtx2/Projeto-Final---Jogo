# Código para definição dos assets
import pygame
import os 
from config import IMG_DIR, SND_DIR, FNT_DIR, PINGUIMD_WIDTH, PINGUIMD_HEIGHT, \
    PINGUIMP_WIDTH, PINGUIMP_HEIGHT, SALMAOC_WIDTH, SALMAOC_HEIGHT, SALMAOD_WIDTH, \
        SALMAOD_HEIGHT, BOMBA_PEDRA_WIDTH, BOMBA_PEDRA_HEIGHT, WIDTH, HEIGHT
   
    
# Define imagens do jogo:   
BACKGROUND = 'background_img'

BACKGROUND_2 = 'background_2_img'
  
INIT_BACKGROUND = 'init_background_img'

INSTRUCOES = 'instrucoes_img'

END = 'end_img'

PINGUIMD_IMG = 'pinguim_deitado_img'
PINGUIMD_FLIP_IMG = 'pinguim_deitado_flip_img'

PINGUIMP_IMG = 'pinguim_em_pe_img'
PINGUIMP_FLIP_IMG = 'pinguim_em_pe_flip_img'

SALMAOC_IMG = 'salmao_carne_img'

SALMAOD_IMG = 'salmaozao_desenho_img'

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

GLOBAL_WARMING_1 = 'global_warming_1_img'
GLOBAL_WARMING_2 = 'global_warming_2_img'
GLOBAL_WARMING_3 = 'global_warming_3_img'
GLOBAL_WARMING_4 = 'global_warming_4_img'
GLOBAL_WARMING_5 = 'global_warming_5_img'
GLOBAL_WARMING_6 = 'global_warming_6_img'

# Define sons do jogo:
EXPLOSAO_SND = 'explosao_arcade_snd'

PINGUIM_GRITO_SND = 'pinguim_grito_snd'

PINGUIM_MORREU_SND = 'pinguim_morreu_snd'

VENTO_SND = 'vento_snd'
MUSICA_JOGO_SND = 'musica_do_jogo_snd'
MUSICA_INICIAL_SND = 'musica_inicial_snd'
PODER_SND = 'poder_snd'
MORDIDA_SND = 'mordida_snd'

# Define fontes do jogo:
SCORE_FONT = 'score_font'

VIDA_FONT = 'vida_font'
INIT_FONT = 'init_font'
INIT_FONT_2 = 'init_font_2'
INIT_FONT_3 = 'init_font_3'
SCORE_FONT_END = 'score_font_end'


# Função principal que carrega os assets:
def load_assets():
    assets = {}

    #Carrega as imagens utilizadas:
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'fundo neve igloo.jpg')).convert()
    assets[BACKGROUND] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))

    assets[BACKGROUND_2] = pygame.image.load(os.path.join(IMG_DIR, 'background_2.png')).convert()
    assets[BACKGROUND_2] = pygame.transform.scale(assets[BACKGROUND_2], (WIDTH, HEIGHT))

    assets[INIT_BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'init background.png')).convert()
    assets[INIT_BACKGROUND] = pygame.transform.scale(assets[INIT_BACKGROUND], (WIDTH, HEIGHT))

    assets[INSTRUCOES] = pygame.image.load(os.path.join(IMG_DIR, 'instrucoes.png')).convert()
    assets[INSTRUCOES] = pygame.transform.scale(assets[INSTRUCOES], (WIDTH, HEIGHT))

    assets[END] = pygame.image.load(os.path.join(IMG_DIR, 'end_screen.png')).convert()
    assets[END] = pygame.transform.scale(assets[END], (WIDTH, HEIGHT))

    assets[PINGUIMD_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'pinguim deitado.png')).convert_alpha()
    assets[PINGUIMD_IMG] = pygame.transform.scale(assets['pinguim_deitado_img'], (PINGUIMD_WIDTH, PINGUIMD_HEIGHT))
    assets[PINGUIMD_FLIP_IMG] = pygame.transform.flip(assets['pinguim_deitado_img'], True, False)

    assets[PINGUIMP_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'pinguim em pe.png')).convert_alpha()
    assets[PINGUIMP_IMG] = pygame.transform.scale(assets['pinguim_em_pe_img'], (PINGUIMP_WIDTH, PINGUIMP_HEIGHT))
    assets[PINGUIMP_FLIP_IMG] = pygame.transform.flip(assets['pinguim_em_pe_img'], True, False)

    assets[PINGUIMPP_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'pinguim poderoso em pe.png')).convert_alpha()
    assets[PINGUIMPP_IMG] = pygame.transform.scale(assets['pinguim_poderoso_em_pe_img'], (PINGUIMP_WIDTH, PINGUIMP_HEIGHT))
    assets[PINGUIMPP_FLIP_IMG] = pygame.transform.flip(assets['pinguim_poderoso_em_pe_img'], True, False)

    assets[PINGUIMPD_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'pinguim poderoso deitado.png')).convert_alpha()
    assets[PINGUIMPD_IMG] = pygame.transform.scale(assets['pinguim_poderoso_deitado_img'], (PINGUIMD_WIDTH, PINGUIMD_HEIGHT))
    assets[PINGUIMPD_FLIP_IMG] = pygame.transform.flip(assets['pinguim_poderoso_deitado_img'], True, False)

    assets[SALMAOC_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'salmao carne.png')).convert_alpha()
    assets[SALMAOC_IMG] = pygame.transform.scale(assets['salmao_carne_img'], (SALMAOC_WIDTH, SALMAOC_HEIGHT))

    assets[SALMAOD_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'salmao desenho.png')).convert_alpha()
    assets[SALMAOD_IMG] = pygame.transform.scale(assets[SALMAOD_IMG], (SALMAOD_WIDTH, SALMAOD_HEIGHT))

    assets[BOMBA_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'bomba desenho.png')).convert_alpha()
    assets[BOMBA_IMG] = pygame.transform.scale(assets['bomba_img'], (SALMAOD_WIDTH, SALMAOD_HEIGHT))
    
    assets[PEDRA_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'pedra desenho.png')).convert_alpha()
    assets[PEDRA_IMG] = pygame.transform.scale(assets['pedra_img'], (SALMAOD_WIDTH, SALMAOD_HEIGHT))

    assets[GLOBAL_WARMING_1] = pygame.image.load(os.path.join(IMG_DIR, 'AQUECIMENTO_GLOBAL_1.jpg')).convert_alpha()
    assets[GLOBAL_WARMING_1] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))

    assets[GLOBAL_WARMING_2] = pygame.image.load(os.path.join(IMG_DIR, 'AQUECIMENTO_GLOBAL_2.jpg')).convert_alpha()
    assets[GLOBAL_WARMING_2] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))

    assets[GLOBAL_WARMING_3] = pygame.image.load(os.path.join(IMG_DIR, 'AQUECIMENTO_GLOBAL_3.jpg')).convert_alpha()
    assets[GLOBAL_WARMING_3] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))

    assets[GLOBAL_WARMING_4] = pygame.image.load(os.path.join(IMG_DIR, 'AQUECIMENTO_GLOBAL_4.jpg')).convert_alpha()
    assets[GLOBAL_WARMING_4] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))

    assets[GLOBAL_WARMING_5] = pygame.image.load(os.path.join(IMG_DIR, 'AQUECIMENTO_GLOBAL_5.jpg')).convert_alpha()
    assets[GLOBAL_WARMING_5] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))

    assets[GLOBAL_WARMING_6] = pygame.image.load(os.path.join(IMG_DIR, 'AQUECIMENTO_GLOBAL_6.jpg')).convert_alpha()
    assets[GLOBAL_WARMING_6] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))

    #Carrega os sons:
    
    assets[EXPLOSAO_SND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'explosao-arcade.wav'))
    assets[EXPLOSAO_SND].set_volume(3)
    
    assets[PODER_SND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'som-do-poder.wav'))
    assets[PODER_SND].set_volume(3)
    
    assets[PINGUIM_GRITO_SND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'pinguim_gritou.ogg'))
    assets[PINGUIM_GRITO_SND].set_volume(3)

    assets[PINGUIM_MORREU_SND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'pinguim_RIP.ogg'))
    assets[PINGUIM_MORREU_SND].set_volume(2)
    
    assets[MORDIDA_SND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'mordida-som.wav'))
    assets[MORDIDA_SND].set_volume(1)

    # Carrega as fontes:
    assets[INIT_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'fonte titulo.ttf'), 65)
    
    assets[SCORE_FONT_END] = pygame.font.Font(os.path.join(FNT_DIR, 'score fonte.ttf'), 50)
    
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'score fonte.ttf'), 28)

    assets[VIDA_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)
    
    print(assets[SALMAOD_IMG])

    return assets  


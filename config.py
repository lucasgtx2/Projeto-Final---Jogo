# Configurações
from os import path
   
# Estabelece as pastas que contém imagens, sons e fontes:
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'imagens')

SND_DIR = path.join(path.dirname(__file__), 'assets', 'sons')
 
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'fontes')
   
# Dados gerais do jogo.
WIDTH = 700 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 30 # Frames por segundo

# Define tamanhos dos sprites
PINGUIMD_WIDTH = 80
PINGUIMD_HEIGHT = 27

PINGUIMP_WIDTH = 43.4
PINGUIMP_HEIGHT = 80

SALMAOC_WIDTH = 40
SALMAOC_HEIGHT = 34.5

SALMAOD_WIDTH = 37.5
SALMAOD_HEIGHT = 50

BOMBA_PEDRA_WIDTH = 40 
BOMBA_PEDRA_HEIGHT = 36

# Define algumas variáveis com as cores básicas 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
INSTRUCTIONS = 1
GAME = 2
QUIT = 3
END = 4
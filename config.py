#configurações
from os import path
  
# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'imagens')

SND_DIR = path.join(path.dirname(__file__), 'assets', 'sons')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'fontes')
  
# Dados gerais do jogo.
WIDTH = 800 # Largura da tela
HEIGHT = 700 # Altura da tela
FPS = 30 # Frames por segundo

# Define tamanhos
PINGUIMD_WIDTH = 80
PINGUIMD_HEIGHT = 60
PINGUIMP_WIDTH = 60
PINGUIMP_HEIGHT = 80
SALMAOC_WIDTH = 50
SALMAOC_HEIGHT = 38
SALMAOD_WIDTH = 50
SALMAOD_HEIGHT = 38
BOMBA_PEDRA_WIDTH = 50 
BOMBA_PEDRA_HEIGHT = 50

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2
END = 3


  
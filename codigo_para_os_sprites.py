#código para os sprites
import random
import pygame
from config import IMG_DIR, SND_DIR,PINGUIMD_WIDTH, PINGUIMD_HEIGHT, \
    PINGUIMP_WIDTH, PINGUIMP_HEIGHT, SALMAOC_WIDTH, SALMAOC_HEIGHT, SALMAOD_WIDTH, \
        SALMAOD_HEIGHT, BOMBA_PEDRA_WIDTH, BOMBA_PEDRA_HEIGHT, WIDTH, HEIGHT
from assets import *
from pinguim_game_screen import * 

class Pinguim(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Diferentes imagens do pinguim:
        pinguins = [assets[PINGUIMP_IMG], assets[PINGUIMP_FLIP_IMG], assets[PINGUIMD_IMG], assets[PINGUIMD_FLIP_IMG], \
            assets[PINGUIMPP_IMG], assets[PINGUIMPP_FLIP_IMG], assets[PINGUIMPD_IMG], assets[PINGUIMPD_FLIP_IMG]]
                #assets[PINGUIMGORDOP_IMG], assets[PINGUIMGORDOP_FLIP_IMG], assets[PINGUIMGORDOD_IMG], assets[PINGUIMGORDOD_FLIP_IMG]]

        # Estrutura para organizar imagens dos pinguins conforme estados:
        self.images = {
            'NORMAL': {
                'PARADO': {
                    'ESQUERDA': pinguins[0],
                    'DIREITA': pinguins[1]
                },
                'DESLIZANDO': {
                    'ESQUERDA': pinguins[2],
                    'DIREITA': pinguins[3]
                }
            },
            'PODEROSO': {
                'PARADO': { 
                    'ESQUERDA': pinguins[4],
                    'DIREITA': pinguins[5]
                },
                'DESLIZANDO': {
                    'ESQUERDA': pinguins[6],
                    'DIREITA': pinguins[7]
                }
            }
        }

        # Dedfinição dos estados do pinguim:
        self.state1 = 'NORMAL'
        self.state2 = 'PARADO'
        self.state3 = 'DIREITA'

        # Define imagem conforme estados:
        self.image = self.images[self.state1][self.state2][self.state3]
        self.mask = pygame.mask.from_surface(self.image)

        # Define posição do pinguim:
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - PINGUIMP_HEIGHT

        self.speedx = 0

        self.assets = assets

        # Calcula tempo para limitar a frequência de poder: 
        self.ultimo_poder = pygame.time.get_ticks()
        self.poder_ticks = random.randint(20000, 30000)

    def update(self):
        # Atualização da posição do pinguim
        self.rect.x += self.speedx

        # Atualiza imagens
        bottom = self.rect.bottom
        x = self.rect.centerx
        self.image = self.images[self.state1][self.state2][self.state3]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = bottom

        # Mantem dentro da tela:
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0  
        

        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.ultimo_poder
        
        # Se já acabou o tempo do poder:
        if elapsed_ticks > self.poder_ticks:
           self.state1 = 'NORMAL'   

class Carne(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[SALMAOC_IMG]
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - SALMAOC_WIDTH)
        self.rect.y = random.randint(-100, -SALMAOC_HEIGHT)

        self.speedy = random.randint(3, 5)

    def update(self):
        # Atualizando a posição do pinguim
        self.rect.y += self.speedy
        
        # Se a carne passar do final da tela, volta para cima e sorteia
            # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH - SALMAOC_WIDTH)
            self.rect.y = random.randint(-100, -SALMAOC_HEIGHT)
            self.speedy = random.randint(3, 5)

class Pedra(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[PEDRA_IMG]
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - BOMBA_PEDRA_WIDTH)
        self.rect.y = random.randint(-100, -BOMBA_PEDRA_HEIGHT)

        self.speedx = random.randint(-2, 2)
        self.speedy = random.randint(3, 5)

    def update(self):
        # Atualizando a posição da pedra
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # Se a pedra bater na parede, ricocheteia com a velocidade contrária em x
        if self.rect.right > WIDTH:
            self.speedx = -self.speedx
        
        if self.rect.left < 0:
            self.speedx = -self.speedx
        
        # Se a carne passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH - BOMBA_PEDRA_WIDTH)
            self.rect.y = random.randint(-100, - BOMBA_PEDRA_HEIGHT)
            self.speedy = random.randint(3, 7)

class Bomba(pygame.sprite.Sprite):
    def __init__(self, assets, groups):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[BOMBA_IMG]

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - BOMBA_PEDRA_WIDTH)
        self.rect.y = random.randint(-100, - BOMBA_PEDRA_HEIGHT)

        self.speedy = 5

        self.groups = groups

        self.assets = assets

    def update(self):
        # Atualizando a posição da bomba
        self.rect.y += self.speedy

class Salmaozao(pygame.sprite.Sprite):
    def __init__(self, groups,  assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        print(assets)
        self.image = assets[SALMAOD_IMG]

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - SALMAOD_WIDTH)
        self.rect.y = random.randint(-100, -  SALMAOD_HEIGHT)

        self.speedx = random.randint(-2, 2)
        self.speedy = 5

        self.groups = groups

        self.assets = assets
    

    def update(self):
        # Atualizando a posição dO SALMAOZAO
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Se o salmao bater na parede, ricocheteia com a velocidade contrária em x
        if self.rect.right > WIDTH:
            self.speedx = -self.speedx
        
        if self.rect.left < 0:
            self.speedx = -self.speedx
    
    
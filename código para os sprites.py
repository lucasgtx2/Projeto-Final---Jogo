#código para os sprites
import random
import pygame
from config import IMG_DIR, SND_DIR,PINGUIMD_WIDTH, PINGUIMD_HEIGHT, \
    PINGUIMP_WIDTH, PINGUIMP_HEIGHT, SALMAOC_WIDTH, SALMAOC_HEIGHT, SALMAOD_WIDTH, \
        SALMAOD_HEIGHT, BOMBA_PEDRA_WIDTH, BOMBA_PEDRA_HEIGHT
from assets import *
  
#Classe do Pinguim
class Pinguim(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        pinguins = [assets[PINGUIMP_IMG, PINGUIMD_IMG]]
        
        self.images = {
            PARADO = pinguins[0]
            DESLIZANDO = pinguins[1]
        }

        self.state = PARADO
        self.image = self.images[PARADO]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - PINGUIMP_HEIGHT

        self.speedx = 0
        self.groups = groups
        self.assets = assets

    def update(self):
        # Atualização da posição do pinguim
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Carne(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[SALMAOC_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - SALMAOC_WIDTH)
        self.rect.y = random.randint(-100, -SALMAOC_HEIGHT)
        self.speedy = random.randint(2, 9)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.y += self.speedy
        # Se a carne passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH - SALMAOC_WIDTH)
            self.rect.y = random.randint(-100, -SALMAOC_HEIGHT)
            self.speedy = random.randint(2, 9)

class Pedra(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[PEDRA_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - PEDRA_WIDTH)
        self.rect.y = random.randint(-100, -PEDRA_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(7, 15)

    def update(self):
        # Atualizando a posição da pedra
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # Se a pedra bater na parede, ricocheteia com a velocidade contrária em x
        if self.rect.right > WIDTH:
            self.speedx = -self.speedx
        
        # Se a carne passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH - PEDRA_WIDTH)
            self.rect.y = random.randint(-100, -PEDRA_HEIGHT)
            self.speedy = random.randint(7, 15)

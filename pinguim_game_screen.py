# Game screen
import pygame
import random
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, END, QUIT, GAME
from codigo_para_os_sprites import Pinguim, Carne, Salmaozao, Pedra, Bomba
from assets import *
 
# Função que coordena o funcionamento do jogo: 
def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()
 
    #Criando grupos com os sprites:
    all_sprites = pygame.sprite.Group()
    all_carnes = pygame.sprite.Group()
    all_pedras = pygame.sprite.Group()
    all_bombas = pygame.sprite.Group()
    all_salmao_inteiros = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_carnes'] = all_carnes
    groups['all_pedras'] = all_pedras
    groups['all_bombas'] = all_bombas
    groups['all_salmao_inteiros'] = all_salmao_inteiros

    # Criando o jogador:
    player = Pinguim(assets)
    all_sprites.add(player)
    
    # Criando as carnes (salmão):
    for carne in range(4):
        carne = Carne(assets)
        all_sprites.add(carne)
        all_carnes.add(carne)

    #Criando pedras:
    for i in range(2):
        pedra = Pedra(assets)
        all_pedras.add(pedra)
        all_sprites.add(pedra)

    #Criando bomba:
    #bomba = Bomba(assets, groups)
    #all_bombas.add(bomba)
    #all_sprites.add(bomba)

    state = GAME

    keys_down = {}
    
    score = 0
    lives = 3
    
    # Só será possível cair uma bomba entre 20 e 30s
    ultima_bomba = pygame.time.get_ticks()
    bomba_ticks = random.randint(10000, 15000)

    ultimo_salmaozao = pygame.time.get_ticks()
    salmaozao_ticks = random.randint(20000, 30000)

    pygame.mixer.music.play(loops=-1)
    
    # ===== Loop principal =====
    while state != QUIT and state != END:
        clock.tick(FPS)
        
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                return QUIT
            
            # Só verifica o teclado se está no estado de jogo
            if state == GAME:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    player.state2 = 'DESLIZANDO'
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        
                        player.state3 = 'ESQUERDA'
                        
                        if player.state1 == 'NORMAL':
                            player.speedx -= 7
                        
                        if player.state1 == 'PODEROSO':
                            player.speedx -= 12
                        
                    if event.key == pygame.K_RIGHT:
                        
                        player.state3 = 'DIREITA'
                        
                        if player.state1 == 'NORMAL':
                            player.speedx += 7
                        
                        if player.state1 == 'PODEROSO':
                            player.speedx += 12

                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    player.state2 = 'PARADO'
                    # Dependendo da tecla, altera a velocidade.
                    if event.key in keys_down and keys_down[event.key]:
                        if player.state1 == 'NORMAL':
                            if player.state3 == 'ESQUERDA': 
                                player.speedx += 7
                            if player.state3 == 'DIREITA':
                                player.speedx -= 7
                        if player.state1 == 'PODEROSO':
                            if player.state3 == 'ESQUERDA': 
                                player.speedx += 12
                            if player.state3 == 'DIREITA':
                                player.speedx -= 12
                
                #Corrige bug 
                if player.state1 == 'NORMAL':
                    if player.speedx < -7 or player.speedx > 7:
                        player.speedx = 0
                
                if player.state1 == 'PODEROSO':
                    if player.speedx < -12 or player.speedx > 12:
                        player.speedx = 0

        # ----- Atualiza estado do jogo:
        
        # Atualizando a posição dos sprites:
        all_sprites.update()
        
        if state == GAME:
            # Verifica se pode cair
            now_B = pygame.time.get_ticks()
            # Verifica quantos ticks se passaram desde a última queda.
            elapsed_ticks_B = now_B - ultima_bomba
            
            # Se já pode cair novamente...
            if elapsed_ticks_B > bomba_ticks:
                # Marca o tick da nova imagem.
                ultima_bomba = now_B
                # A nova bomba vai ser criada no topo da tela
                nova_bomba = Bomba(assets, groups)
                groups['all_sprites'].add(nova_bomba)
                groups['all_bombas'].add(nova_bomba)
                bomba_ticks = random.randint(10000, 15000)
            
            #Verifica se pode criar no salmaozao:
            now_S = pygame.time.get_ticks()
            # Verifica quantos ticks se passaram desde a última queda.
            elapsed_ticks_S = now_S - ultimo_salmaozao

            # Se já pode cair novamente...
            if elapsed_ticks_S > salmaozao_ticks:
                # Marca o tick da nova imagem.
                ultimo_salmaozao = now_S
                # A nova bomba vai ser criada no topo da tela
                novo_salmaozao = Salmaozao(assets, groups)
                groups['all_sprites'].add(novo_salmaozao)
                groups['all_salmao_inteiros'].add(novo_salmaozao)
                salmaozao_ticks = random.randint(10000, 15000)

            # Verifica se o pinguim comeu pedaço de carne:
            comeu = pygame.sprite.spritecollide(player, all_carnes, True, pygame.sprite.collide_mask)
            for carne in comeu: # As chaves são os elementos do primeiro grupo (salmao) que colidiram com o penguim
                # O salmao e destruido e precisa ser recriado
                assets[MORDIDA_SND].play()
                carne = Carne(assets)
                all_sprites.add(carne)
                all_carnes.add(carne)
            
            
                # Ganhou pontos!
                if player.state1 == 'PODEROSO':
                    score += 150
                else:
                    score += 100
                
                if score % 5000 == 0:
                    lives += 1
                

            # Verifica se houve colisão entre pinguim e pedra
            hits = pygame.sprite.spritecollide(player, all_pedras, True, pygame.sprite.collide_mask)
            for pedra in hits:
                # A pedra e destruido e precisa ser recriado
                assets[PINGUIM_GRITO_SND].play()
                pedra = Pedra(assets)
                all_sprites.add(pedra)
                all_pedras.add(pedra)

                # Perdeu pontos e vida
                score -= 200
                lives -= 1
                
            # Verifica se houve colisão entre pinguim e bomba
            hits = pygame.sprite.spritecollide(player, all_bombas, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                assets[EXPLOSAO_SND].play()
                b = Bomba(assets, groups)
                all_sprites.add(b)
                all_bombas.add(b)
                player.kill()
                state = END
                lives = 0

            # Verifica se pinguim comeu o salmãozão:  
            poder = pygame.sprite.spritecollide(player, all_salmao_inteiros, True, pygame.sprite.collide_mask)
            if len(poder) == 1:
                all_sprites.remove(salmao_inteiro)
                salmao_inteiro = Salmaozao(groups, assets)
                all_sprites.add(salmao_inteiro)
                all_salmao_inteiros.add(salmao_inteiro)
                player.state1 = 'PODEROSO'
                player.speedx = 0

        
        if lives == 0:
            state = END

        # ----- Gera saídas
        if score < 7500:
            window.blit(assets[BACKGROUND], (0, 0))
        else:
            window.blit(assets[BACKGROUND_2], (0, 0))
        
        # Desenhando todos os sprites:
        all_sprites.draw(window)

        # Desenhando o score:
        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        # Desenhando as vidas:
        text_rect = text_surface.get_rect()
        text_surface = assets[VIDA_FONT].render(chr(9829) * lives, True, RED)
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state, score  
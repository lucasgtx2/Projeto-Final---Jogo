#game screen
import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, END, QUIT
from assets import load_assets
from codigo_para_os_sprites import Pinguim, Carne, Salmaozao, Pedra, Bomba


def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()
 
    #Criando grupos com os sprites:
    all_sprites = pygame.sprite.Group()
    all_carnes = pygame.sprite.Group()
    all_pedras = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_carnes'] = all_carnes
    groups['all_pedras'] = all_pedras

    # Criando o jogador
    player = Pinguim(groups, assets)
    all_sprites.add(player)
    # Criando as carnes (salmão)
    for i in range(6):
        carne = Carne(assets)
        all_sprites.add(carne)
        all_carnes.add(carne)

    #Criando salmão inteiro:
    salmao_inteiro = Salmaozao(groups, assets)
    all_sprites.add(salmao_inteiro)

    #Criando pedras:
    for i in range(3):
        pedra = Pedra(groups, assets)
        all_pedras.add(pedra)
        all_sprites.add(pedra)

    #Criando bomba:
    bomba = Bomba(groups, assets)
    all_sprites.add(bomba)

    DONE = 0
    PLAYING = 1
    DEAD = 2
    state = PLAYING

    keys_down = {}
    score = 0
    lives = 3
      
    # ===== Loop principal =====
    pygame.mixer.music.play(loops=-1)
    while state != DONE or state != END:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
                return QUIT
            
            # Só verifica o teclado se está no estado de jogo
            if state == PLAYING:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    Pinguim.state2 = 'DESLIZANDO'
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 20
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 20
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    Pinguim.state2 = 'PARADO'
                    # Dependendo da tecla, altera a velocidade.
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx += 8
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 8
                
        # ----- Atualiza estado do jogo
        # Atualizando a posição dos obstaculos
        all_sprites.update()

        if state == PLAYING:
            # Verifica se o pinguim comeu pedaço de carne
            hits = pygame.sprite.groupcollide(all_carnes, player, True, True, pygame.sprite.collide_mask)
            for carne in hits: # As chaves são os elementos do primeiro grupo (salmao) que colidiram com o penguim
                # O salmao e destruido e precisa ser recriado
                assets[MORDIDA_SND].play()
                s = Carne(assets)
                all_sprites.add(s)
                all_carnes.add(s)
            

                # Ganhou pontos!
                score += 100
                if score % 1000 == 0:
                    lives += 1

            # Verifica se houve colisão entre pinguim e pedra
            hits = pygame.sprite.spritecollide(player, all_pedras, True, pygame.sprite.collide_mask)
            for pedra in hits:
                # O salmao e destruido e precisa ser recriado
                assets[PEDRA_SND].play()
                p = Pedra(assets)
                all_sprites.add(p)
                all_carnes.add(p)

                # Perdeu uma vida!
                lives -= 1
                
            # Verifica se houve colisão entre pinguim e bomba
            hits = pygame.sprite.spritecollide(player, bomba, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                assets[EXPLOSAO_SND].play()
                b = Bomba(assets)
                all_sprites.add(b)
                player.kill()
                lives = 0
                state = END

        # HITS PINGUIM PODEROSO COM SALMAOZAO
            hits = pygame.sprite.spritecollide(player, salmao_inteiro, True, pygame.sprite.collide_mask)
            if len(hits) == 1:
                assets[PODER_SND].play()
                salmao_inteiro = Salmaozao(assets)
                all_sprites.add(salmao_inteiro)
                Pinguim.state1 = 'PODEROSO'

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor preto
        window.blit(assets[BACKGROUND], (0, 0))
        
        # Desenhando todos os sprites
        all_sprites.draw(window)

        # Desenhando o score
        text_surface = assets[INIT_FONT].render("{:08d}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        # Desenhando as vidas
        text_surface = assets[INIT_FONT].render(chr(9829) * lives, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador

        return state
                                                
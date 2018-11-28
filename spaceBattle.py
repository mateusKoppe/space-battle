import pygame

from player import Player
from enemy import EnemiesList
from configs import gameConfigs
from projectile import ProjectileList, ProjectileEnemiesList

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((gameConfigs["width"], gameConfigs["height"]))

pygame.display.set_caption(gameConfigs["title"])

fontSmall = pygame.font.Font("assets/fonts/bitcell.ttf", 20)
fontLarge = pygame.font.Font("assets/fonts/bitcell.ttf", 200)

run = True

player = Player(screen)
EnemiesList.randomSpawn(screen)
while run:
    clock.tick(60)
    screen.fill((0, 0, 0))

    vidas = fontSmall.render("Vidas: "+str(player.lifes), True, (255,255,255))
    screen.blit(vidas, (10,10))

    inimigos = fontSmall.render("Inimigos: "+str(len(EnemiesList.enemies)), True, (255,255,255))
    screen.blit(inimigos, (10,25))

    inimigos = fontSmall.render("Tempo: "+str(pygame.time.get_ticks()/1000), True, (255,255,255))
    screen.blit(inimigos, (10,40))

    if len(EnemiesList.enemies)<=0:
        screen.fill((0, 0, 0))
        screen.blit(fontLarge.render("Venceu!", True, (255,255,255)), (gameConfigs["width"]/2 - 240, gameConfigs["height"]/2  - 100))
    
    elif player.lifes<=0:
        screen.fill((0, 0, 0))
        screen.blit(fontLarge.render("Perdeu!", True, (255,255,255)), (gameConfigs["width"]/2 - 240, gameConfigs["height"]/2  - 100))
    
    else:        
        player.update()
        ProjectileList.update()
        ProjectileEnemiesList.update()
        EnemiesList.update()

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
    pygame.display.update()
    
pygame.quit()
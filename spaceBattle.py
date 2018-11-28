import pygame

from background import Background
from player import Player
from ship import Ship
from enemy import EnemiesList, Enemy
from configs import gameConfigs
from projectile import ProjectileList, ProjectileEnemiesList, Projectile


pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((gameConfigs["width"], gameConfigs["height"]))

pygame.display.set_caption(gameConfigs["title"])

fontSmall = pygame.font.Font("assets/fonts/bitcell.ttf", 30)
fontLarge = pygame.font.Font("assets/fonts/bitcell.ttf", 200)

run = True

actualLevel = 1

def handle_speed():
    global actualLevel

    time = pygame.time.get_ticks() // 1000
    steep = time // gameConfigs["timeToIncreaseSpeed"]
    print(steep)
    if steep > actualLevel:
        actualLevel += 1
        if (Ship.speed <= gameConfigs["maxSpeed"]):
            Ship.speedUp()
            Enemy.speedUp()
            Projectile.speedUp()

player = Player(screen)
EnemiesList.randomSpawn(screen)
Background.init(screen)
while run:
    clock.tick(60)
    screen.fill((0, 0, 0))

    if len(EnemiesList.enemies)<=0:
        screen.blit(fontLarge.render("Venceu!", True, (255,255,255)), (gameConfigs["width"]/2 - 240, gameConfigs["height"]/2  - 100))
    
    elif player.lifes<=0:
        pygame.mixer.music.load("assets/audios/gunshot2.ogg")
        pygame.mixer.music.play()
        screen.blit(fontLarge.render("Perdeu!", True, (255,255,255)), (gameConfigs["width"]/2 - 240, gameConfigs["height"]/2  - 100))
    
    else:        

        Background.update(screen)
        player.update()
        ProjectileList.update()
        ProjectileEnemiesList.update()
        EnemiesList.update()

    
    lifesImage = pygame.image.load("assets/images/lifes.png")
    lifesText = fontSmall.render(": "+str(player.lifes), True, (255,255,255))

    # screen.blit(lifesText, (45,110))
    tam = 40
    for i in range(player.lifes):
        screen.blit(lifesImage, (800, tam))
        tam += 30
        

    enemiesText = fontSmall.render("Inimigos: "+str(len(EnemiesList.enemies)), True, (255,255,255))
    # screen.blit(enemiesText, (10, 145))

    timeText = fontSmall.render("Tempo: "+str(pygame.time.get_ticks()/1000), True, (255,255,255))
    # screen.blit(timeText, (10, 160))

    handle_speed()

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
    pygame.display.update()
    
pygame.quit()
import pygame

from player import Player
from enemy import EnemiesList
from configs import gameConfigs
from projectile import ProjectileList

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((gameConfigs["width"], gameConfigs["height"]))

pygame.display.set_caption(gameConfigs["title"])

run = True

player = Player(screen)
EnemiesList.randomSpawn(screen)
while run:
    clock.tick(60)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    player.update()
    ProjectileList.update()
    EnemiesList.update()
    pygame.display.update()
    
pygame.quit()
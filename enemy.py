import pygame
import random
from ship import Ship
from projectile import Projectile, ProjectileList
from configs import gameConfigs

class EnemiesList():
    enemies = []

    def update():
        for enemy in EnemiesList.enemies:
            enemy.update()

    def add(enemy):
        EnemiesList.enemies.append(enemy)

    def randomSpawn(screen):
        y = 10
        x = random.randint(0, gameConfigs["width"] - Enemy.width)
        enemy = Enemy(screen, (x, y))
        EnemiesList.add(enemy)

class Enemy(Ship):
    def __init__(self, screen, pos):
        image = pygame.image.load("assets/enemy-ship.png")
        super().__init__(screen, pos, image)

    def update(self):
        if (self.x > gameConfigs["width"]):
            self.x = 0

        self.x += self.speed

        self.render()
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
    
    def remove(enemy):
        EnemiesList.enemies.remove(enemy)

    def randomSpawn(screen):
        y = 10
        x = random.randint(0, gameConfigs["width"] - Enemy.width)
        enemy = Enemy(screen, (x, y))
        EnemiesList.add(enemy)

class Enemy(Ship):
    def __init__(self, screen, pos):
        image = pygame.image.load("assets/enemy-ship.png")
        super().__init__(screen, pos, image)

    def check_dead(self):
        for projectile in ProjectileList.projectiles:
            isInY = projectile.y > self.y and projectile.y < self.y + self.height - 5
            isInX = projectile.x > self.x and projectile.x < self.x + self.width
            if isInX and isInY:
                EnemiesList.remove(self)

    def update(self):
        if (self.x > gameConfigs["width"]):
            self.x = 0

        self.x += self.speed

        self.check_dead()

        self.render()
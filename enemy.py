import pygame
import random
from ship import Ship
from projectile import Projectile, ProjectileList
from configs import gameConfigs

class Enemy(Ship):
    def __init__(self, screen):
        y = self.height + 10
        x = random.randint(0, gameConfigs["width"] - self.width)
        image = pygame.image.load("assets/enemy-ship.png")
        super().__init__(screen, (x, y), image)

    def update(self):
        if (self.x > gameConfigs["width"]):
            self.x = 0

        self.x += self.speed

        self.render()
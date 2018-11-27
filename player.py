import pygame
from ship import Ship
from projectile import Projectile, ProjectileList
from configs import gameConfigs

class Player(Ship):
    def __init__(self, screen):
        y = gameConfigs["height"] - self.height - 10
        x = gameConfigs["width"] // 2 - self.width // 2
        image = pygame.image.load("assets/player-ship.png")
        super().__init__(screen, (x, y), image)

    def update(self):
        self.gunLastShot += 1

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if keys[pygame.K_SPACE] and self.gunLastShot > self.gunDelay:
            self.gunLastShot = 0
            projectile = Projectile(self.screen, (self.x + self.width // 2, self.y), Projectile.UP)
            ProjectileList.projectiles.append(projectile)

        self.render()
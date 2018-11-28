import pygame

class ProjectileList:
    projectiles = []

    def update():
        for projectile in ProjectileList.projectiles:
            projectile.update()

class ProjectileEnemiesList:
    projectiles = []

    def update():
        for projectile in ProjectileEnemiesList.projectiles:
            projectile.update()

    def remove(projectile):
        ProjectileEnemiesList.projectiles.remove(projectile)

class Projectile:
    UP = "UP"
    DOWN = "DOWN"
    speed = 15

    def __init__(self, screen, position, direction):
        self.direction = direction
        self.x, self.y = position
        self.screen = screen

    def render(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x, self.y), 5)

    def update(self):
        if (self.direction == self.UP):
            self.y -= self.speed
        if (self.direction == self.DOWN):
            self.y += self.speed

        self.render()

    def speedUp():
        Projectile.speed += 2
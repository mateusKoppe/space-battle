import pygame
import random
from ship import Ship
from projectile import Projectile, ProjectileList, ProjectileEnemiesList
from configs import gameConfigs

class EnemiesList():
    enemies = []
    lastSpawn = 0

    def update():
        for enemy in EnemiesList.enemies:
            enemy.update()

    def add(enemy):
        EnemiesList.enemies.append(enemy)
        EnemiesList.lastSpawn = pygame.time.get_ticks()/1000
    
    def remove(enemy):
        EnemiesList.enemies.remove(enemy)

    def randomSpawn(screen):
        y = 10
        x = random.randint(0, gameConfigs["width"] - Enemy.width)
        enemy = Enemy(screen, (x, y))
        EnemiesList.add(enemy)

class Enemy(Ship):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    direction = random.choice([LEFT, RIGHT])
    directionTime = 0
    speed = 4

    def __init__(self, screen, pos):
        image = pygame.image.load("assets/images/enemy-ship.png")
        super().__init__(screen, pos, image)

    def check_dead(self):
        for projectile in ProjectileList.projectiles:
            isInY = projectile.y > self.y and projectile.y < self.y + self.height - 5
            isInX = projectile.x > self.x and projectile.x < self.x + self.width
            if isInX and isInY:
                pygame.mixer.music.load("assets/audios/explosion.mp3")
                pygame.mixer.music.play()
                EnemiesList.remove(self)

    def toggleDirection(self):
        if self.direction == Enemy.LEFT:
            self.direction = Enemy.RIGHT
        elif self.direction == Enemy.RIGHT:
            self.direction = Enemy.LEFT
    
    def resetDirectionTime(self):
        self.directionTime = 0

    def steep(self):
        if (self.direction == Enemy.LEFT):
            self.x -= self.speed
        elif (self.direction == Enemy.RIGHT):
            self.x += self.speed

    def update(self):
        self.steep()
        self.directionTime += 1

        if (pygame.time.get_ticks()/1000 > EnemiesList.lastSpawn+5):
            EnemiesList.randomSpawn(self.screen)    

        if random.randint(0,1000) < 20:
            pygame.mixer.music.load("assets/audios/gunshot2.mp3")
            pygame.mixer.music.play()
            projectile = Projectile(self.screen, (self.x + self.width // 2, self.y), Projectile.DOWN)
            ProjectileEnemiesList.projectiles.append(projectile)

        isInLeftBorder = self.x <= 0
        isInRigthBorder = self.x >= gameConfigs["width"] - self.width
        if isInLeftBorder or isInRigthBorder:
            self.toggleDirection()
            

        maxRand = gameConfigs["width"] // 2 + (self.directionTime * 3) // 1
        valueToToggle = random.randint(gameConfigs["width"] // 3, maxRand)

        if valueToToggle > gameConfigs["width"]:
            self.toggleDirection()
            self.resetDirectionTime()

        self.check_dead()

        super().update()
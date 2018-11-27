import pygame

pygame.init()

screen = {
    "width": 850,
    "height": 600,
}

projectiles = []

speed = 5

clock = pygame.time.Clock()

window = pygame.display.set_mode((screen["width"], screen["height"]))

pygame.display.set_caption("Space battle")

class Ship:
    width = 71
    height = 85
    gunLastShot = 0
    gunDelay = 25

    def __init__(self, x, y, image):
        self.y = 0
        self.x = 0
        self.image = image

    def render(self):
        window.blit(self.image, (self.x, self.y))

class Player(Ship):
    def __init__(self):
        self.y = screen["height"] - self.height - 10
        self.x = screen["width"] // 2 - self.width // 2
        self.image = pygame.image.load("assets/player-ship.png")

    def update(self):
        self.gunLastShot += 1

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= speed

        if keys[pygame.K_RIGHT]:
            self.x += speed

        if keys[pygame.K_SPACE] and self.gunLastShot > self.gunDelay:
            self.gunLastShot = 0
            projectile = Projectile((self.x + self.width // 2, self.y), Projectile.UP)
            projectiles.append(projectile)

        self.render()

class Projectile:
    UP = "UP"
    DOWN = "DOWN"
    speed = 15

    def __init__(self, position, direction):
        self.direction = direction
        self.x, self.y = position

    def render(self):
        pygame.draw.circle(window, (255, 255, 255), (self.x, self.y), 5)

    def update(self):
        if (self.direction == self.UP):
            self.y -= self.speed
        if (self.direction == self.DOWN):
            self.y += self.speed

        self.render()

def projectiles_update():
    for projectile in projectiles:
        print(projectile.x)
        projectile.update()

run = True
player = Player()
while run:
    clock.tick(60)
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player.update()
    projectiles_update()
    pygame.display.update()
    
pygame.quit()
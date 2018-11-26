import pygame

pygame.init()

screen = {
    "width": 850,
    "height": 600,
}

speed = 5

clock = pygame.time.Clock()

window = pygame.display.set_mode((screen["width"], screen["height"]))

pygame.display.set_caption("Space battle")

class Ship:
    width = 71
    height = 85

    def __init__(self, x, y, image):
        self.y = 0
        self.x = 0
        self.image = image

    def render(self):
        window.blit(self.image, (self.x, self.y))

class Player(Ship):
    def __init__(self):
        self.y = screen["height"] - self.height - 10
        self.x = screen["width"] / 2 - self.width / 2
        self.image = pygame.image.load("assets/player-ship.png")

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= speed

        if keys[pygame.K_RIGHT]:
            self.x += speed

run = True
player = Player()
while run:
    clock.tick(60)
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player.update()
    pygame.display.update()
    
pygame.quit()
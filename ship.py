class Ship:
    width = 71
    height = 85
    gunLastShot = 0
    gunDelay = 25
    speed = 5

    def __init__(self, screen, pos, image):
        self.x, self.y = pos
        self.image = image
        self.screen = screen

    def render(self):
        self.screen.blit(self.image, (self.x, self.y))
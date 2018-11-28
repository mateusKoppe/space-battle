from configs import gameConfigs

class Ship:
    width = 40
    height = 48
    gunLastShot = 0
    gunDelay = 25
    speed = 5

    def __init__(self, screen, pos, image):
        self.x, self.y = pos
        self.image = image
        self.screen = screen

    def update(self):
        if (self.x >= gameConfigs["width"] - self.width):
            self.x = gameConfigs["width"] - self.width

        if (self.x <= 0):
            self.x = 0

        print(self.speed)
        self.render()

    def render(self):
        self.screen.blit(self.image, (self.x, self.y))
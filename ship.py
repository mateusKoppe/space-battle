from configs import gameConfigs

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

    def update(self):
        if (self.x >= gameConfigs["width"] - self.width):
            self.x = gameConfigs["width"] - self.width

        if (self.x <= 0):
            self.x = 0
            
        self.render()

    def render(self):
        self.screen.blit(self.image, (self.x, self.y))

    def speedUp():
        if (Ship.speed <= gameConfigs["maxSpeed"]):
            Ship.speed += 1
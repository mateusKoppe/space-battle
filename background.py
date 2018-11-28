import pygame

from configs import gameConfigs

class Background:
    speedBackground = 0
    speedClouds = 0
    positionX = -50
    positionY = -(4500-600)
    positionXClouds = -100

    image = pygame.image.load("assets/images/brasilia.jpg")
    # image = pygame.image.load("assets/images/background.jpeg")
    clouds = pygame.image.load("assets/images/backgroundClouds.png")

    def init(screen):
        screen.blit(Background.image, (Background.positionX,Background.positionY))
        screen.blit(Background.clouds, (Background.positionX,100))
        

    def update(screen):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            Background.speedBackground +=0.005
            Background.speedClouds +=0.01
        
        if keys[pygame.K_RIGHT]:
            Background.speedBackground -=0.005
            Background.speedClouds -=0.01


        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            Background.speedBackground = 0
            Background.speedClouds = 0  

        if Background.positionX  <= -100:
            Background.positionX = -100
        if Background.positionX >= 0:
            Background.positionX = 0

        if Background.positionXClouds  <= -200:
            Background.positionXClouds = -200
        if Background.positionXClouds >= 0:
            Background.positionXClouds = 0
        
        if Background.positionY >= 0:
            Background.positionY = -(4500-600)

        Background.positionX += Background.speedBackground
        Background.positionY += 5
        Background.positionXClouds += Background.speedClouds
        Background.render(screen)

    def render(screen):
        screen.blit(Background.image, (Background.positionX, Background.positionY))
        screen.blit(Background.clouds, (Background.positionXClouds, 0))
        
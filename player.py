import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.attack = 10
        self.velocity = 6
        self.image = pygame.image.load('PygameAssets-main/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 500

    def moveRight(self):
        self.rect.x += self.velocity

    def moveLeft(self):
        self.rect.x -= self.velocity

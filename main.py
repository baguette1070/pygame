import pygame
from game import Game


pygame.init()

pygame.display.set_caption("Nawfal")
screen = pygame.display.set_mode((1480, 720))

background = pygame.image.load("PygameAssets-main/bg.jpg")
game = Game()

running = True

while running:

    screen.blit(background, (0, -200))

    screen.blit(game.player.image, game.player.rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("droite")
                game.player.moveRight()
            elif event.key == pygame.K_LEFT:
                print("gauche")
                game.player.moveLeft()
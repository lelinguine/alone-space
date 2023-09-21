import pygame, sys, pygame.camera
from lib.game.Game import Game

pygame.init()

pygame.display.set_caption("Alone in Space")
pygame_icon = pygame.image.load('assets/alternative.png')
pygame.display.set_icon(pygame_icon)
screen = pygame.display.set_mode((1280, 736))

clock = pygame.time.Clock()
delta = 0

game = Game(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game.update(delta)

    pygame.display.flip()
    pygame.display.update()
    delta = clock.tick(90) / 1000
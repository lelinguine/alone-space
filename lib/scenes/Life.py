import pygame

class Life:

    def __init__(self, player):
        self.player = player

    def update(self, screen):
        x = 54
        pos = 0

        for i in range(0, self.player.life):
            image = pygame.image.load(f"assets/life/0.png")
            screen.blit(image, (x*pos, 0))
            pos += 1

        for i in range(pos, 3):
            image = pygame.image.load(f"assets/life/1.png")
            screen.blit(image, (x*pos, 0))
            pos += 1

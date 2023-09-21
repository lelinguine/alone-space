import pygame

class Platform:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)

    def update(self, screen, variant):
        self.rect.x += variant

        self.surface.fill(self.color)
        screen.blit(self.surface, self.rect.topleft)

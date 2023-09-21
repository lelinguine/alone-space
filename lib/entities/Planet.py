from typing import Any
import pygame
from lib.entities.Animate import Animate


class Planet(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        self.image = None
        self.animate = Animate(self, "planet")
        self.rect = self.image.get_rect(center=((x/2), y/2))

        self.hflip = True
        self.vflip = False

    def update(self, delta):
        self.animate.idle(delta) 
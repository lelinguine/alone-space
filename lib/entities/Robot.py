from typing import Any
import pygame
from lib.entities.Animate import Animate

from lib.config import debug

class Robot(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        self.image = None
        self.animate = Animate(self, "robot")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.hflip = True
        self.vflip = False
        self._gravity = 100
        self._flip = 1

        self.speed = 0
        self.life = 2 #max 3

    def update(self, delta):
        self.move(delta)

    def move(self, delta):
        keys = pygame.key.get_pressed()
        self.animate.idle(delta)
        self.speed = 200

        #debug
        if debug:
            if keys[pygame.K_z]:
                self.animate.walk(delta)
                self.rect.y -= 500*delta

            if keys[pygame.K_s]:
                self.animate.walk(delta)
                self.rect.y += 500*delta
            if(keys[pygame.K_g]):
                self._flip = self._flip * -1

        #movements
        if keys[pygame.K_q]:
            if keys[pygame.K_LSHIFT]:
                self.speed = self.speed *1.8
                self.animate.run(delta)
            else:
                self.animate.walk(delta)
            self.left(delta * self.speed)
        if keys[pygame.K_d]:
            if keys[pygame.K_LSHIFT]:
                self.speed = self.speed *1.8
                self.animate.run(delta)
            else:
                self.animate.walk(delta)
            self.right(delta * self.speed)

        self.gravity(delta)

    #direction
    def left(self, speed):
        self.rect.x -= speed
        if(self.hflip) :
            self.hflip = not self.hflip
    def right(self, speed):
        self.rect.x += speed
        if(not self.hflip) :
            self.hflip = not self.hflip

    #gravity
    def gravity(self, delta):
        self.rect.y += self._gravity * self._flip * delta
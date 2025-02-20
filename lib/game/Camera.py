import pygame

class Camera:

    def __init__(self, background, player, map):

        self.player = player
        self.background =  background
        self.map = map
        self.x = 0
        self.variant = 0

    def update(self, delta, width, place):

        speed = self.player.speed*delta
        scroll = 400
        marge = 20
        
        keys = pygame.key.get_pressed()
        if self.player.rect.x < scroll and keys[pygame.K_q] and self.background.x + self.variant + marge < 0:
            self.variant = speed
            self.player.rect.x = scroll
        elif self.player.rect.x > width - scroll - self.player.image.get_width() and keys[pygame.K_d] and self.background.x + self.variant - marge > (self.background.width - width) * -1:
            self.variant = -speed
            self.player.rect.x = width - scroll - self.player.image.get_width()
        else:
            self.variant = 0
            
        self.background.draw_background(self.variant, width, place)
        self.map.update(self.variant)
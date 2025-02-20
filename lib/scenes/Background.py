import pygame

class Background:

    def __init__(self, screen, path):
        self.layers = 2
        self.path = path
        self.screen = screen
        self.x = 0
        self.background = []
        for i in range(0, self.layers):
            image = pygame.image.load(self.path + f"{i}.png").convert_alpha()
            self.background.append(image)

            if i == 1:
                self.width = image.get_width()

    def draw_background(self, variant, width, place):
        if place == "outside":
            self.screen.fill((184,228,248))
        else:
            self.screen.fill((0,0,0))
        
        scale = 0

        if self.x + variant > 0:
            variant = 0
        if self.x + variant < (self.width - width) * -1 :
            variant = 0

        self.x += variant

        for i in self.background:
            scale += 0.5
            self.screen.blit(i, (self.x * scale, 0))
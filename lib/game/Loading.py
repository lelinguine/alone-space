import pygame

class Loading:
    def __init__(self, player, screen):
        self.screen = screen
        self.player = player

        self.x = (screen.get_width()) - 100
        self.y = (screen.get_height()) - 200
        self.largeur_rect = 50
        self.hauteur_rect = 100
        self.couleur_rect = (0, 0, 0)

        self.rect = pygame.Rect(self.x, self.y, self.largeur_rect, self.hauteur_rect)

    def update(self, load, place):
        pygame.draw.rect(self.screen, self.couleur_rect, self.rect)

        if self.player.rect.colliderect(self.rect):
            self.loading(load, place)

    def loading(self, load, place):
        
        if place == "outside":
            load("inside")
        elif place == "inside":
            load("introduction")

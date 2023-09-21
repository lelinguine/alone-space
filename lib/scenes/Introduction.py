import pygame
from lib.scenes.Title import Title
from lib.entities.Planet import Planet

class Introduction:

    def __init__(self, screen, load):
        self.screen = screen
        self.place = "introduction"
        self.load = load

        #title
        self.title = Title()
        self.title.cumulate = 50
        self.title.color = (255,255,255)

        #subtitle
        self.subtitle = Title()
        self.subtitle.cumulate = 50
        self.subtitle.color = (255,255,255)

        #planet
        self.planet = Planet(screen.get_width(), screen.get_height())
        self.entities = pygame.sprite.Group()
        self.entities.add(self.planet)

        #background
        self.background = pygame.image.load("assets/space.png")
        self.w, self.h =  self.background.get_size()
        self.x = 0
        self.x1 = self.w*-1
        
        #music
        pygame.mixer.music.load(f'assets/scenes/{self.place}/ambiant.mp3')
        pygame.mixer.music.play(-1)

    def update(self, delta):

        #load outside
        keys = pygame.key.get_pressed()
        if any(keys) and not keys[pygame.K_ESCAPE]:
            self.load("outside")

        #background
        self.x1 -= 1
        self.x -= 1
        self.screen.blit(self.background,(self.x , 0))
        self.screen.blit(self.background,(self.x1 , 0))
        if self.x < -self.w:
            self.x = self.w
        if self.x1 < -self.w:
            self.x1 = self.w
        
        #planet
        self.entities.update(delta)
        self.entities.draw(self.screen)

        #title
        self.title.stroke(self.screen, 80, "Alone in Space", 0, "poppin")
        self.subtitle.flow(self.screen, 24, "Press any key to continue", -(self.screen.get_height()-100), "poppin", delta)


        

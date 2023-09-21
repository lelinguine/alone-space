import pygame
from lib.entities.Robot import Robot
from lib.game.Camera import Camera
from lib.scenes.Background import Background
from lib.scenes.Title import Title
from lib.game.Physic import Physic
from lib.scenes.Map import Map

from lib.config import debug

class Scene:

    def __init__(self, screen, load, place):
        self.screen = screen
        self.place = place
        self.load = load
        
        #entities
        self.player = Robot(550,550)
        self.entities = pygame.sprite.Group()
        self.entities.add(self.player)

        #camera
        self.background = Background(screen, f"assets/scenes/{self.place}/")
        self.map = Map(self.screen)
        self.map.outside(self.background.width, screen.get_height())
        self.camera = Camera(self.background, self.player, self.map)
        if not debug:
            self.title = Title()

        #physic
        self.physic = Physic(self.player, self.map)

        #music
        pygame.mixer.music.load(f'assets/scenes/{self.place}/ambiant.mp3')
        pygame.mixer.music.play(-1)

    def update(self, delta):
        #load introdution on click
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.load("introduction")
        if keys[pygame.K_RETURN] and self.place == "outside":
            self.load("inside")

        self.entities.update(delta)
        self.camera.update(delta, self.screen.get_width(), self.place)

        self.physic.update(delta)

        self.entities.draw(self.screen)

        if not debug:
            if self.place == "outside":
                self.title.update(delta, self.screen, "Lonely PLanet", "Welcome")
            elif self.place == "inside":
                self.title.update(delta, self.screen, "Lost Cave", "Welcome")
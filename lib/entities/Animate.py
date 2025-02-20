import pygame, json

from lib.config import debug

class Animate:
    # Constructor
    def __init__(self, entity, animate):

        self.entity = entity

        self._animate = animate

        self.frame = 0
        self._idle = []
        self._run = []

        self.start()

    # Initialize Animations
    def start(self):
        self.set(self._idle, "idle")

    # Set Assets with json
    def set(self, assets, animation):
        if len(assets) == 0:
            with open(f'assets/{self._animate}/config.json', 'r') as fichier_json:
                data = json.load(fichier_json)
                data = data['{}'.format(animation)]
                frames = int(data["frames"])

            for i in range(frames):
                assets.append(pygame.image.load(f"assets/{self._animate}" + '/{}/'.format(animation)+'{}.png'.format(i)))
            
            if self.entity.image == None:
                self.entity.image = assets[self.frame]

        

    # Animate
    def animate(self, assets, speed):
        self.frame += speed
        if int(self.frame) >= len(assets):
            self.frame = 0
        self.entity.image = assets[int(self.frame)]

        #debug
        if debug:
            self.entity.image.fill((255, 255, 255, 255))

        #hflip
        if self.entity.hflip:
            self.entity.image = pygame.transform.flip(self.entity.image, True, False)
        #vflip
        if self.entity.vflip:
            self.entity.image = pygame.transform.flip(self.entity.image, False, True)


    # Idle Animation
    def idle(self, delta):
        self.animate(self._idle, delta * 8)
    
    # Walk Animation
    def walk(self, delta):
        self.idle(delta * 1.2)

    # Run Animation
    def run(self, delta):
        if self._run ==[]:
            self.set(self._run, "run")
        self.animate(self._run, delta * 8)
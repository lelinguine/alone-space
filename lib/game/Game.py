from lib.scenes.Introduction import Introduction
from lib.scenes.Scene import Scene

class Game:

    def __init__(self, screen):
        self.screen = screen
        self.scene = Introduction(screen, self.load)
        
    def load(self, scene):
        if scene == "introduction":
            self.scene = Introduction(self.screen, self.load)
        elif scene == "outside":
            self.scene = Scene(self.screen, self.load, "outside")
        elif scene == "inside":
            self.scene = Scene(self.screen, self.load, "inside")

    def update(self, delta):
        self.scene.update(delta)



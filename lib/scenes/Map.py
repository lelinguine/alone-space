from lib.entities.Platform import Platform

from lib.config import debug

class Map:
    def __init__(self, screen):
        self.platforms = []
        self.screen = screen

    def outside(self, width, height):
        bloc = 32

        for i in range(1, int(round(width/bloc))-1):
            self.platform = Platform(bloc * i, height - bloc * 2, bloc, bloc, self.color(i))
            self.platforms.append(self.platform)

        for i in range(1, int(round(width/bloc))-1):
            self.platform = Platform(bloc * i, 0, bloc, bloc, self.color(i))
            self.platforms.append(self.platform)

        for i in range(1, int(round(height/bloc))-1):
            self.platform = Platform(0, bloc * i, bloc, bloc, self.color(i))
            self.platforms.append(self.platform)

        for i in range(1, int(round(height/bloc))-1):
            self.platform = Platform(width-bloc, bloc * i, bloc, bloc, self.color(i))
            self.platforms.append(self.platform)

        if debug:
            for i in range(1, int(round(640/bloc))):
                self.platform = Platform(bloc*i+800, 400, bloc, bloc, self.color(i))
                self.platforms.append(self.platform)

    def update(self, variant):

        for platform in self.platforms:
            platform.update(self.screen, int(round(variant)))

    def color(self, i):
        if debug:
            if i % 2 == 0:
                return (0, 255, 0, 255)
            else:
                return (0, 0, 255, 255)
        return (255, 255, 255, 0)
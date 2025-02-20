import pygame
from pygame import *

class Title:
    def __init__(self):
        font.init()
        self.isCumulate = True
        self.cumulate = 0
        self.color = (0,0,0)

        self._flow = 0
        self._isFlow = False

    def update(self, delta, screen, title, subtitle):
        if self.cumulate < 4 and self.isCumulate:
            self.cumulate += delta
        else:
            self.isCumulate = False
            self.cumulate -= delta

        self.draw(screen, 24, f"{subtitle}", 110, "poppin")
        self.draw(screen, 96, f"{title}", 0, "poppin")

    def draw(self, screen, size, text, pos, police):
        font = pygame.font.Font(f"assets/font/{police}.otf", size)
        text = font.render(text, True, self.color)
        text.set_alpha(100 *self.cumulate)
        text_rect = text.get_rect(center=(screen.get_width()/2, (screen.get_height()-pos)/2))
        if self.color == (0, 0, 0):
            self.draw_bar(screen, screen.get_height()-64)
            self.draw_bar(screen, 0)
        screen.blit(text, text_rect) 

    #cinematic
    def draw_bar(self, screen, pos):
        bar = pygame.Surface((screen.get_width(),64))
        bar.set_alpha(1000*self.cumulate)
        bar.fill(self.color)
        screen.blit(bar, (0,pos))

    #flow
    def flow(self, screen, size, text, pos, police, delta):

        speed = 10
        if self._flow <= 0 and not self._isFlow:
            self._isFlow = True
            self._flow += delta * 10
        elif self._flow >= speed and self._isFlow:
            self._flow -= delta * 10
            self._isFlow = False
        elif self._isFlow:
            self._flow += delta * 10
        elif not self._isFlow:
            self._flow -= delta * 10

        font = pygame.font.Font(f"assets/font/{police}.otf", size)
        text = font.render(text, True, self.color)
        text.set_alpha(40 * self._flow)
        text_rect = text.get_rect(center=(screen.get_width()/2, (screen.get_height()-pos)/2))
        screen.blit(text, text_rect)  

    #stroke
    def stroke(self, screen, size, text, pos, police):
        font = pygame.font.Font(f"assets/font/{police}.otf", size)
        text = self.render(text, font)
        text_rect = text.get_rect(center=(screen.get_width()/2, (screen.get_height()-pos)/2))
        screen.blit(text, text_rect)  

    def render(self, text, font, gfcolor=(0, 0, 0), ocolor=(255, 255, 255), opx=4):
            textsurface = font.render(text, True, gfcolor).convert_alpha()
            w = textsurface.get_width() + 2 * opx
            h = font.get_height()

            osurf = pygame.Surface((w, h + 2 * opx)).convert_alpha()
            osurf.fill((0, 0, 0, 0))

            surf = osurf.copy()

            osurf.blit(font.render(text, True, ocolor).convert_alpha(), (0, 0))

            for dx, dy in self._circlepoints(opx):
                surf.blit(osurf, (dx + opx, dy + opx))

            surf.blit(textsurface, (opx, opx))
            return surf
    
    def _circlepoints(self, r):
        _circle_cache = {}
        r = int(round(r))
        if r in _circle_cache:
            return _circle_cache[r]
        x, y, e = r, 0, 1 - r
        _circle_cache[r] = points = []
        while x >= y:
            points.append((x, y))
            y += 1
            if e < 0:
                e += 2 * y - 1
            else:
                x -= 1
                e += 2 * (y - x) - 1
        points += [(y, x) for x, y in points if x > y]
        points += [(-x, y) for x, y in points if x]
        points += [(x, -y) for x, y in points if y]
        points.sort()
        return points

    



class Physic:
    def __init__(self, player, map):
        self.player = player
        self.platforms = map.platforms

    def update(self, delta):
        repulse = (self.player._gravity/5) * delta
        marge = 20
        scale = 20
        for objet in self.platforms:
            if self.player.rect.colliderect(objet.rect):

                if (self.player.rect.midbottom[1] - marge < objet.rect.midtop[1]):
                    self.player.rect.y -= repulse * (scale/4)

                elif (self.player.rect.midtop[1] + marge > objet.rect.midbottom[1]):
                    self.player.rect.y += repulse * (scale/4)

                elif (self.player.rect.midright[0] - marge < objet.rect.midleft[0]):
                    self.player.rect.x -= repulse * scale

                elif (self.player.rect.midleft[0] + marge > objet.rect.midright[0]):
                    self.player.rect.x += repulse * scale

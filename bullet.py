import pygame

class Bullet:
    def __init__(self, x, y, w, h, speed, texture):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.hit_box = self.texture.get_rect()
        self.hit_box.x = x
        self.hit_box.y = y
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.sound_shoot = pygame.mixer.Sound("explosion_01-6225.mp3")
        self.sound_shoot.play(-1)
        self.sound_shoot.set_volume(0)

    def render(self, window):
        window.blit(self.texture, (self.hit_box.x, self.hit_box.y))

    def movement(self):
        
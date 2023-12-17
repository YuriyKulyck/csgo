import pygame

class Hero:
    def __init__(self, x, y, w, h, texture, speedX):
        self.speedX = speedX
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.hit_box = self.texture.get_rect()
        self.hit_box.x = x
        self.hit_box.y = y
        self.texture = pygame.transform.scale(self.texture, (w, h))

    def render(self, window):
        window.blit(self.texture, (self.hit_box.x, self.hit_box.y))

    def movement(self):
        keys = pygame.key.get_pressed()
        is_step = False
        if keys[pygame.K_d]:
            if self.hit_box.x < 550:
                self.hit_box.x += self.speed
                is_step = True
        if keys[pygame.K_a]:
            if self.hit_box.x > 0:
                self.hit_box.x -= self.speed
                is_step = True

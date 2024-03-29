import pygame
import bullet


class Hero:
    def __init__(self, x, y, w, h, texture, speed):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.hit_box = self.texture.get_rect()
        self.hit_box.x = x
        self.hit_box.y = y
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.magazine = []
        self.sound_shoot = pygame.mixer.Sound("explosion_01-6225.mp3")



    def render(self, window):
        window.blit(self.texture, (self.hit_box.x, self.hit_box.y))
        for bullet in self.magazine:
            bullet.movement()
            bullet.render(window)

    def movement(self):
        keys = pygame.key.get_pressed()
        is_step = False
        if keys[pygame.K_d]:
            if self.hit_box.x < 550:
                self.hit_box.x += self.speed
        if keys[pygame.K_a]:
            if self.hit_box.x > 0:
                self.hit_box.x -= self.speed

    def shoot(self):
        keys2 = pygame.key.get_pressed()
        if keys2[pygame.K_r]:
            self.magazine.append(bullet.Bullet(self.hit_box.x, self.hit_box.y, 20, 20, 5, "bullet.png"))

            self.sound_shoot.play()
            return True
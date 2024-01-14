import pygame
import random
import time
import hero
import enemy
from settings import fire_sound

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("space.ogg")
pygame.mixer.music.play(-1)

window = pygame.display.set_mode((600, 700))
fps = pygame.time.Clock()

layout = pygame.image.load("galaxy.jpg")
layout = pygame.transform.scale(layout, (600, 700))

shootsound = pygame.mixer.Sound(fire_sound)


N1LIGHT = hero.Hero(275, 600, 50, 75, "rocket.png", 6)
lichbul = -1
bullsit = []
fixtime1 = time.time()
fixtime2 = time.time()
enemyrange = []
for i in range(25):
    enemyrange.append(enemy.Enemy(random.randint(50, 550), random.randint(-1000, 0), 50, 50, 2, "asteroid.png"))

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    for enemy in enemyrange:
        enemy.movement()

    N1LIGHT.movement()

    for colbul in bullsit:
        lichbul +=1
        lich  = -1
        for colenem in enemyrange:
            lich += 1
            if colbul.hitbox.colliderect(colenem.hitbox):
                try:
                    enemyrange.pop(lich)
                    bullsit.pop(lichbul)
                except:
                    pass
    lichbul = -1


    window.blit(layout, (0, 0))
    N1LIGHT.render(window)
    for enemy in enemyrange:
        enemy.render(window)
    pygame.display.flip()
    fps.tick(60)
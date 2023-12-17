import pygame
import random
import time

import hero

pygame.init()

window = pygame.display.set_mode((600, 700))
fps = pygame.time.Clock()

layout = pygame.image.load("galaxy.jpg")
layout = pygame.transform.scale(layout, (600, 700))
xyiloN1 = hero.Hero(275, 600, 75, 75, "rocket.png", 1.5)

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    window.blit(layout, (0, 0))
    xyiloN1.render(window)
    pygame.display.flip()
    fps.tick(60)
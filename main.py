import json

import pygame
import random
import time
import hero
import enemy

def startgame():
    def read_data():
        global settings
        with open("settings.json", "r", encoding="utf-8") as file:
            settings = json.load(file)
    read_data()

    pygame.init()

    pygame.mixer.init()
    pygame.mixer.music.load("space.ogg")
    pygame.mixer.music.play(-1)

    window = pygame.display.set_mode((600, 700))
    fps = pygame.time.Clock()

    layout = pygame.image.load("galaxy.jpg")
    layout = pygame.transform.scale(layout, (600, 700))

    shootsound = pygame.mixer.Sound("hq-explosion-6288.mp3")


    N1LIGHT = hero.Hero(275, 600, 50, 75, settings["skin"], 6)
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
                return

        N1LIGHT.shoot()

        for i in enemyrange:
            i.movement()

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
        for i in enemyrange:
            i.render(window)
        pygame.display.flip()
        fps.tick(60)


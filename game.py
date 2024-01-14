import pygame
import enemy
import hero
import bullet
import time
import random
import settings

def start():

    pygame.init()
    pygame.mixer.init()
    window = pygame.display.set_mode((800, 500))
    fps = pygame.time.Clock()

    fon = pygame.image.load(settings.fon_texture)
    fon = pygame.transform.scale(fon, (800, 500))
    fonlose = pygame.image.load(settings.lose_texture)
    fonlose = pygame.transform.scale(fonlose, (800, 500))
    fonwin = pygame.image.load(settings.win_texture)
    fonwin = pygame.transform.scale(fonwin, (800, 500))

    pygame.mixer.music.load(settings.music)
    shootsound = pygame.mixer.Sound(settings.fire_sound)
    islose = False
    iswin = False
    lichbul = -1
    bullsit = []
    enmylist = []
    fixtime1 = time.time()
    fixtime2 = time.time()
    nmet  = 0

    pygame.mixer.music.play(-1)

    N1LIGHT = hero.Hero(300, 400, 100, 100, settings.rocket_texture, player_speed )

    for i in range(asteroid_count):
        enmylist.append(enemes.Enemy(random.randint(0, 750), random.randint(-100 * asteroid_count, 0),asteroid_size, asteroid_size,
                                     asteroid_speed , settings.mateor_texture1 , settings.mateor_texture2 , settings.mateor_texture3 ,
                                     random.randint(1 ,3)))

    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()

        rocket.move()
        rocket.shoot()
        # print(rocket.shoot())
        if rocket.shoot() == True:
            if time.time() - fixtime1 > 0.5:
                fixtime1 = time.time()
                shootsound.play()
                bullsit.append(bullets.Bullshit(rocket.hitbox.x + 45, rocket.hitbox.y, 15, 30, settings.bull_texture,
                                                bull_speed))

        for enemy1 in enmylist:
            if rocket.hitbox.colliderect(enemy1.hitbox):
                # game = False
                # pygame.quit()
                islose = True
                losesound.play()
                shootsound.set_volume(0)
                bomsound.set_volume(0)
                rocket.hitbox.x = 10000
                rocket.hitbox.y = 10000
                pygame.mixer.music.stop()
                #pygame.mixer.quit()

        for colbul in bullsit:
            lichbul += 1
            lich = -1
            for colenem in enmylist:
                lich += 1
                if colbul.hitbox.colliderect(colenem.hitbox):
                    nmet +=1
                    text1 = f1.render('Збито: ' + str(nmet) + " " + "з " + str(asteroid_count), 1, (180, 0, 0))
                    try:
                        enmylist.pop(lich)
                        bullsit.pop(lichbul)
                        bomsound.play()
                    except:
                        pass
        lichbul = -1

        for item in bullsit:
            if item.hitbox.y < 0:
                bullsit.pop(0)

        if time.time() - fixtime2 > asteroid_count:
            iswin = True
            text2 = f1.render('Результат: ' + str(nmet) + " " + "з " + str(asteroid_count), 1, (200, 200, 200))
            shootsound.set_volume(0)
            pygame.mixer.music.stop()
            if time.time() - fixtime2 < asteroid_count + 0.02:
                winsound.play()
            #pygame.mixer.quit()

        window.fill((255, 0, 0))
        window.blit(fon, [0, 0])
        rocket.render(window)

        for enemy in enmylist:
            enemy.move()
            enemy.render(window)

        for bull in bullsit:
            bull.move()
            bull.render(window)

        window.blit(text1, (10, 10))

        if iswin == True:
            window.blit(fonwin, [0, 0])
            window.blit(text2 , (100 , 200))
        if islose == True:
            window.blit(fonlose, [0, 0])

        pygame.display.flip()
        fps.tick(fps1)
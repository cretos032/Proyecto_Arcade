import pygame, math, sys, Clases, random
from pygame.locals import*
pygame.init()

#Definimos Variables
size=(1280, 720)
speedx=speedy=0
position = [0, 360]
black=(0,0,0)
kright=kleft=kup=kdown=0
bullets=[]
aliens=[]
lasers=[]
car=Clases.Car()
throw=False
r=True
dispr=None
clock=pygame.time.Clock()
t=0


#seteamos la pantalla
screen=pygame.display.set_mode(size, FULLSCREEN)

#Básico del juego
while 1:
    clock.tick(30)
    t+=1
    al=random.random()*100
    for event in pygame.event.get():
        if hasattr(event, 'key')==False:
            continue
        down = event.type == KEYDOWN
        if event.key==K_RIGHT:
            kright=down*10
            r=True
        elif event.key==K_LEFT:
            kleft=down*-10
            r=False
        elif event.key==K_UP:
            kup=down*-10
        elif event.key==K_DOWN:
            kdown=down*10
        elif event.key==K_ESCAPE:
            pygame.quit()
            sys.exit(0)
        if event.key == K_SPACE:
            throw=True
    screen.fill(black)

    #Iniciamos la simulacion
    speedx=(kleft+kright)
    speedy=(kup+kdown)
    x, y=position
    x += speedx
    y += speedy
    position=[x,y]
    if speedx>=0 and r==True:
        car.move(position[0], position[1])
        if t>=150:
            if throw == True:
                bullets.append(Clases.Bullet(car.rect.centerx, car.rect.centery, True))
                throw=False
            if al<=2:
                aliens.append(Clases.Alien(car.rect.centery, 1280))
        r=True
        for alien in aliens:
            if alien.rect.centery==car.rect.centery:
                if alien.rect.centerx-car.rect.centerx < 0:
                    dispr=True
                elif alien.rect.centerx-car.rect.centerx > 0:
                    dispr=False
                lasers.append(Clases.Laser(alien.rect.centerx, alien.rect.centery, dispr))
        screen.blit(car.image, car.rect)
    elif speedx<=0 and r==False:
        car.move(position[0], position[1])
        if throw == True:
            bullets.append(Clases.Bullet(car.rect.centerx, car.rect.centery, False))
            throw = False
        if al<=2:
            aliens.append(Clases.Alien(car.rect.centery, 1280))
        r=False
        for alien in aliens:
            if alien.rect.centery==car.rect.centery:
                if alien.rect.centerx-car.rect.centerx < 0:
                    dispr=True
                elif alien.rect.centerx-car.rect.centerx > 0:
                    dispr=False
                lasers.append(Clases.Laser(alien.rect.centerx, alien.rect.centery, dispr))
        screen.blit(car.image1, car.rect)
    for bullet in bullets:
        screen.blit(bullet.image, bullet.rect)
        bullet.update()
        if bullet.rect.right > 1280 or bullet.rect.left < 0:
            bullet.__del__()
    for alien in aliens:
        if alien.vivo==True:
            screen.blit(alien.image, alien.rect)
            alien.update()
            if alien.rect.right>1280 or alien.rect.left<0:
                alien.__del__()
    for laser in lasers:
        if laser.vivo==True:
            screen.blit(laser.image, laser.rect)
            laser.update()
            if laser.rect.left<0 or laser.rect.right>1280:
                laser.__del__()
    for bullet in bullets:
        if bullet.vivo==True:
            for alien in aliens:
                if alien.vivo==True:
                    if pygame.sprite.collide_rect(alien, bullet)==True:
                        bullet.__del__()
                        alien.__del__()
    for bullet in bullets:
        if bullet.vivo==True:
            for laser in lasers:
                if laser.vivo==True:
                    if pygame.sprite.collide_rect(bullet, laser):
                        bullet.__del__()
                        laser.__del__()
    for alien in aliens:
        for laser in lasers:
            if pygame.sprite.collide_rect(car, alien) or pygame.sprite.collide_rect(car, laser):
                pygame.quit()
                sys.exit(0)
    pygame.display.flip()
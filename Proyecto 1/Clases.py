import pygame, random
from pygame.locals import*
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, r):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
        self.speed=20
        self.t=r
        self.vivo=True

    def __del__(self):
        self.vivo=False
        self.rect.centerx=2000

    def update(self):
        if self.t==True:
            self.rect.centerx += self.speed
        elif self.t==False:
            self.rect.centerx -= self.speed

class Alien(pygame.sprite.Sprite):
    def __init__(self, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("alien.png")
        self.rect = self.image.get_rect()
        self.p=random.random()*100
        self.width = self.image.get_width()
        if self.p<50:
            self.rect.centerx=self.width/2
            self.speed=5
        elif self.p>=50:
            self.rect.centerx=size-self.width/2
            self.speed=-5
        self.rect.centery=y
        self.vivo=True

    def __del__(self):
        self.vivo=False
        self.rect.centerx=2000

    def update(self):
        mov=random.random()*100
        self.rect.centerx += self.speed
        if mov>=50:
            self.rect.centery +=self.speed
        elif mov<50:
            self.rect.centery -=self.speed

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, r):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
        self.speed=20
        self.t=r
        self.vivo=True

    def __del__(self):
        self.vivo=False
        self.rect.centerx=2000

    def update(self):
        if self.t==True:
            self.rect.centerx += self.speed
        elif self.t==False:
            self.rect.centerx -= self.speed

class Car(pygame.sprite.Sprite):
    def __init__(self):
        self.image=pygame.image.load("card.png")
        self.image1=pygame.transform.flip(self.image, True, False)
        self.rect=self.image.get_rect()
        self.rect.centerx=0
        self.rect.centery=360

    def move(self, x, y):
        self.rect.centerx=x
        self.rect.centery=y

    def __del__(self):
        self.rect.centerx=2000
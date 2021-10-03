import pygame
from pygame.draw import *

pygame.init()

FPS = 30
sc = pygame.display.set_mode((800, 800))

sc.fill((180,180,180))
circle(sc,(255,255,0),(400,400),200)
circle(sc,(0,0,0),(400,400),200,2)

circle(sc,(255,0,0),(320,350),40)
circle(sc,(0,0,0),(320,350),40,2)
circle(sc,(0,0,0),(320,350),20)

circle(sc,(255,0,0),(480,360),30)
circle(sc,(0,0,0),(480,360),30,2)
circle(sc,(0,0,0),(480,360),15)

sur2 = pygame.Surface((300,300), pygame.SRCALPHA)
rect(sur2,(0,0,0),(0,0,200,30))
sc.blit(pygame.transform.rotate(sur2,-45),(50,200))

sur1 = pygame.Surface((300,300), pygame.SRCALPHA)
rect(sur1,(0,0,0),(0,0,200,10))
sc.blit(pygame.transform.rotate(sur1,35),(400,200))


rect(sc,(0,0,0),(300,500,200,30))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
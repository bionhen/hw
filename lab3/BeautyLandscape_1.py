import pygame
from pygame.draw import *

pygame.init()

FPS = 30
sc = pygame.display.set_mode((800, 1000))
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
DARK_GREEN = (0,100,0)
GREEN = (154,205,50)
PURPLE = (238,130,238)
sc.fill(GREEN)

def flower(): #создаёт surface с цветочком
    sur = pygame.Surface((300,300),pygame.SRCALPHA) #pygame.SRCALPHA - для прозрачного фона
    for i in range(3):
        ellipse(sur,WHITE,(5+25*i,12-12*(i%2),50,25))
        ellipse(sur,BLACK,(5+25*i,12-12*(i%2),50,25), width=1)
    ellipse(sur, YELLOW, (35,20,50,25))
    for i in range(2):
        ellipse(sur,WHITE,(60-12*i,20+i*15,50,25))
        ellipse(sur,BLACK,(60-12*i,20+i*15,50,25), width=1)
    for i in range(2):
        ellipse(sur,WHITE,(20-20*i,35-i*5,50,25))
        ellipse(sur,BLACK,(20-20*i,35-i*5,50,25), width=1)
    return sur

def bush(): #создаёт surface с кустом цветов
    r = 200
    sur = pygame.Surface((2*r,2*r),pygame.SRCALPHA)
    circle(sur,DARK_GREEN,(r,r),r)
    for i in range(3):
        sur.blit(pygame.transform.rotate(
            pygame.transform.scale(
                flower(),(200+50*i,200+50*i)),-30+i*30),
                 (0.3*r,0.3*r))
        
    for i in range(3):
        sur.blit(pygame.transform.rotate(
            pygame.transform.scale(
                flower(),(200+50*i,200+50*i)),-20+i*40),
                 (r,0.3*r))
    return sur

def leg():
    sur = pygame.Surface((500,500),pygame.SRCALPHA)
    ellipse(sur,WHITE,(2,0,50,150))
    ellipse(sur,WHITE,(0,130,55,140))
    ellipse(sur,WHITE,(20,265,50,40))
    return sur

def notunicorn(): #Неопознанное животное
    sur = pygame.Surface((500,500),pygame.SRCALPHA)
    ellipse(sur,WHITE,(200,50,100,50))
    ellipse(sur,WHITE,(200,80,50,150))
    ellipse(sur,WHITE,(0,200,260,120))
    sur.blit(pygame.transform.scale(leg(),(300,300)),(20,280))
    sur.blit(pygame.transform.scale(leg(),(300,300)),(60,300))
    sur.blit(pygame.transform.scale(leg(),(300,300)),(170,270))
    sur.blit(pygame.transform.scale(leg(),(300,300)),(210,290))
    polygon(sur,WHITE,[(200,30),(210,55),(220,59),(210,59),(205,60)])
    polygon(sur,WHITE,[(220,30),(230,52),(240,55),(230,55),(225,53)])
    circle(sur,PURPLE,(240,70),16)
    circle(sur,BLACK,(247,70),7)
    sub = pygame.Surface((15,5),pygame.SRCALPHA)
    ellipse(sub,WHITE,(0,0,15,5))
    sur.blit(pygame.transform.rotate(sub,-30),(230,58))
    return sur

sc.blit(notunicorn(),(200,200))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

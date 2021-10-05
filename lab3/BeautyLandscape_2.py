import pygame
from pygame.draw import *

pygame.init()

FPS = 30
sc = pygame.display.set_mode((800, 1000))
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREEN = (0, 100, 0)
GREEN = (154, 205, 50)
PURPLE = (238, 130, 238)
BLUE = (72, 209, 204)
GREY = (128, 128, 128)
sc.fill(BLUE)


# Задает функцию рисования цветка на объкте Surface с фиксированным размером и переменными цветами
# сol_fl_int - цвет внутренней части
# col_fl_d - цвет границы цветка
# col_fl_ctr - цвет центра цветка


def flower(col_fl_int, col_fl_d, col_fl_ctr):
    sur = pygame.Surface((300, 300), pygame.SRCALPHA)
    for i in range(3):
        ellipse(sur, col_fl_int, (5 + 25 * i, 12 - 12 * (i % 2), 50, 25))
        ellipse(sur, col_fl_d, (5 + 25 * i, 12 - 12 * (i % 2), 50, 25), width=2)
    ellipse(sur, col_fl_ctr, (35, 20, 50, 25))
    for i in range(2):
        ellipse(sur, col_fl_int, (60 - 12 * i, 20 + i * 15, 50, 25))
        ellipse(sur, col_fl_d, (60 - 12 * i, 20 + i * 15, 50, 25), width=2)
    for i in range(2):
        ellipse(sur, col_fl_int, (20 - 20 * i, 35 - i * 5, 50, 25))
        ellipse(sur, col_fl_d, (20 - 20 * i, 35 - i * 5, 50, 25), width=2)
    return sur


# Задает куст на surface
# сol_fl_int - цвет внутренней части
# col_fl_d - цвет границы цветка
# col_fl_ctr - цвет центра цветка
# col_bsh - цвет куста

def bush(col_fl_int, col_fl_d, col_fl_ctr, col_bsh):
    sur = pygame.Surface((400, 400), pygame.SRCALPHA)
    circle(sur, col_bsh, (200, 200), 200)
    for i in range(3):
        sur.blit(pygame.transform.rotate(
            pygame.transform.scale(
                flower(col_fl_int, col_fl_d, col_fl_ctr), (200 + 30 * i, 200 + 30 * i)), -200 + i * 200),
            (30, 30))

    for i in range(3):
        sur.blit(pygame.transform.rotate(
            pygame.transform.scale(
                flower(col_fl_int, col_fl_d, col_fl_ctr), (200 + 30 * i, 300 + 30 * i)), -200 + 30 * i),
            (10, 30))
    return sur


def leg():
    sur = pygame.Surface((500, 500), pygame.SRCALPHA)
    ellipse(sur, WHITE, (2, 0, 50, 150))
    ellipse(sur, WHITE, (0, 130, 55, 140))
    ellipse(sur, WHITE, (20, 265, 50, 40))
    return sur


def notunicorn(col_not):  # создаёт surface с НХЖ(неопознанное ходячее животное)
    sur = pygame.Surface((500, 500), pygame.SRCALPHA)
    ellipse(sur, col_not, (200, 50, 80, 50))
    ellipse(sur, col_not, (200, 80, 50, 150))
    ellipse(sur, col_not, (0, 200, 260, 120))
    sur.blit(pygame.transform.scale(leg(), (300, 300)), (20, 280))
    sur.blit(pygame.transform.scale(leg(), (300, 300)), (60, 300))
    sur.blit(pygame.transform.scale(leg(), (300, 300)), (170, 270))
    sur.blit(pygame.transform.scale(leg(), (300, 300)), (210, 290))
    polygon(sur, col_not, [(200, 30), (210, 55), (220, 59), (210, 59), (205, 60)])
    polygon(sur, col_not, [(220, 30), (230, 52), (240, 55), (230, 55), (225, 53)])
    circle(sur, PURPLE, (240, 70), 16)
    circle(sur, BLACK, (247, 70), 7)
    sub = pygame.Surface((15, 5), pygame.SRCALPHA)
    ellipse(sub, col_not, (0, 0, 15, 5))
    sur.blit(pygame.transform.rotate(sub, -30), (230, 58))
    return sur


polygon(sc, GREY,
        [(0, 300), (0, 1000), (800, 1000), (800, 50), (650, 200), (600, 150), (480, 480), (250, 150), (120, 250),
         (60, 100)])
polygon(sc, BLACK,
        [(0, 300), (0, 1000), (800, 1000), (800, 50), (650, 200), (600, 150), (480, 480), (250, 150), (120, 250),
         (60, 100)], width=2)
polygon(sc, GREEN, [(0, 580), (0, 1000), (800, 1000), (800, 650), (500, 650), (500, 550), (150, 550)])
polygon(sc, BLACK, [(0, 580), (0, 1000), (800, 1000), (800, 650), (500, 650), (500, 550), (150, 550)], width=1)


#Создание кустов


def cr_bush(col_fl_int, col_fl_d, col_fl_ctr, col_bsh, x, y, z, w):
    sc.blit(pygame.transform.scale(bush(col_fl_int, col_fl_d, col_fl_ctr, col_bsh), (x, y)), (z, w))


cr_bush(WHITE, BLACK, YELLOW, DARK_GREEN, 100, 100, -10, 570)
cr_bush(WHITE, BLACK, YELLOW, DARK_GREEN, 300, 300, 530, 750)
cr_bush(WHITE, BLACK, YELLOW, DARK_GREEN, 200, 200, 650, 500)
sc.blit(pygame.transform.scale(bush(WHITE, BLACK, YELLOW, DARK_GREEN), (50, 50)), (430, 530))
sc.blit(pygame.transform.scale(bush(WHITE, BLACK, YELLOW, DARK_GREEN), (75, 75)), (330, 530))
sc.blit(pygame.transform.scale(bush(WHITE, BLACK, YELLOW, DARK_GREEN), (80, 80)), (500, 600))

sc.blit(pygame.transform.scale(notunicorn(WHITE), (700, 700)), (-270, 760))
sc.blit(pygame.transform.scale(notunicorn(WHITE), (150, 150)), (270, 500))
sc.blit(pygame.transform.scale(notunicorn(WHITE), (150, 150)), (190, 600))

sc.blit(pygame.transform.scale(pygame.transform.flip(notunicorn(WHITE), True, False), (100, 100)), (350, 600))
sc.blit(pygame.transform.scale(pygame.transform.flip(notunicorn(WHITE), True, False), (500, 500)), (450, 600))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

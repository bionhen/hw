from random import randint
import turtle

turtle.speed(100)
turtle.penup()
turtle.goto(-300,-300)
turtle.pendown()
turtle.width(5)
for i in range(4):
    turtle.forward(600)
    turtle.left(90)

number_of_turtles = 10
steps_of_time_number = 100


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(100000)
    unit.goto(randint(-300, 300), randint(-300, 300))
    unit.left(randint(1,360))


for i in range(steps_of_time_number):
    for unit in pool:
        x, y = unit.pos()
        if x >= 300:
            unit.left(2*(90-unit.heading()))
        if x <= -300:
            unit.left(2*(90-unit.heading()))
        if y >= 300:
            unit.left(2*(180-unit.heading()))
        if y <= -300:
            unit.left(2*(180-unit.heading()))
        unit.forward(3)

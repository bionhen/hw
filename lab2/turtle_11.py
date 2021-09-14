import turtle as t
import math

def polukrug(r):
    a = r *2* math.sin(math.pi/72)
    for i in range(36):
        t.forward(a)
        t.left(5)
        
def krug(r):
    a = r *2* math.sin(math.pi/72)
    for i in range(72):
        t.forward(a)
        t.left(5)

t.shape('turtle')
t.speed(10)

t.begin_fill()
krug(100)
t.color('yellow')
t.end_fill()

t.color('black')
t.penup()
t.goto(-40,130)
t.pendown()

t.begin_fill()
krug(15)
t.color('blue')
t.end_fill()

t.color('black')
t.penup()
t.goto(40,130)
t.pendown()

t.begin_fill()
krug(15)
t.color('blue')
t.end_fill()

t.width(10)
t.color('black')
t.penup()
t.goto(0,110)
t.pendown()

t.right(90)
t.forward(30)

t.color('red')
t.penup()
t.goto(-70,100)
t.pendown()

polukrug(70)

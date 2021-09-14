import turtle as t
import math

def pr_mng(n, r):
    a = r *2* math.sin(math.pi/n)
    t.left(180/n)
    for i in range(n):
        t.forward(a)
        t.left(360/n)
    t.right(180/n)

t.shape('turtle')
t.speed(10)
for i in range(1,11):
    pr_mng(2+i,30+30*i)
    t.penup()
    t.goto(0, -30*i)
    t.pendown()

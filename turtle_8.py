import turtle as t
import math

def krug(r):
    a = r *2* math.sin(math.pi/72)
    for i in range(72):
        t.forward(a)
        t.left(5)

t.shape('turtle')
t.speed(10)
n=6
for i in range(n):
    krug(100)
    t.left(360/n)
import turtle as t
import math

def krug(r):
    a = r *2* math.sin(math.pi/72)
    for i in range(72):
        t.forward(a)
        t.left(5)

t.shape('turtle')
t.speed(10)
for i in range(20):
    krug(50+20*i)
    t.right(180)
    krug(50+20*i)
    t.right(180)
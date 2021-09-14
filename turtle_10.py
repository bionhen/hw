import turtle as t
import math

def polukrug(r):
    a = r *2* math.sin(math.pi/72)
    for i in range(36):
        t.forward(a)
        t.left(5)

t.shape('turtle')
t.speed(10)
for i in range(10):
    polukrug(50)
    polukrug(10)
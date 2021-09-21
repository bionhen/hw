import turtle as t
from random import *

t.shape('turtle')
t.color('red')
t.speed(10)
for i in range(1000):
    t.forward(100*random())
    t.left(randint(0,180))

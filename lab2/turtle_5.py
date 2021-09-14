import turtle as t

t.shape('turtle')
t.speed(10)
for i in range(1,1000):
    t.forward(1+0.01*i)
    t.left(5)

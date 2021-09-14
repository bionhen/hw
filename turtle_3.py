import turtle as t

t.shape('turtle')
t.speed(10)
for i in range(10):
    for j in range(4):
        t.forward(i*20)
        t.left(90)
    t.penup()
    t.goto(-10*i, -10*i)
    t.pendown()
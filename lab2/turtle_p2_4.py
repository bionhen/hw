import turtle as t

t.shape('circle')
t.speed(0)
t.goto(500,0)
t.goto(-400,0)
x,y = -400, 0
Vx,Vy = 20,60
ay=10
dt = 0.05
k=0.7

for i in range(10000):
    t.goto(x,y)
    x += Vx*dt
    y += Vy*dt
    Vy -= ay*dt
    if y<0:
        Vy = -Vy*k
        Vx = Vx*k
        y=0
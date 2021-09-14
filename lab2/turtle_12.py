import turtle as t
def star(n,a):
    for i in range(n):
        t.forward(a)
        t.left((n-1)/2*360/n)
      
t.shape('turtle')
t.speed(10)
star(11,400)
t.penup()
t.goto(-450,0)
t.pendown()
star(5,400)

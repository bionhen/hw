import turtle as t

def check(a,i):
    if a[i] == 1:
        t.pendown()
    if a[i] == 0:
        t.penup()

def num(a,l):
    k=0
    for i in range(4):
        check(a,k)
        k+=1
        t.forward(l)
        t.left(90)
    t.left(45)
    check(a,k)
    k+=1
    t.forward(l*2**0.5)
    t.left(45)
    for i in range(3):
        check(a,k)
        k+=1
        t.forward(l)
        t.left(90)
    t.left(45)
    check(a,k)
    k+=1
    t.forward(l*2**0.5)
    t.penup()
    t.right(135)
    t.forward(2*l)
    t.left(90)

t.shape('turtle')
t.speed(10)

a0 = [1,1,0,1,0,1,1,1,0]
a1 = [0,1,0,0,0,1,0,0,1]
a2 = [1,0,0,0,1,1,1,0,0]
a3 = [1,1,1,0,0,1,1,0,0]
a4 = [0,1,1,0,0,1,0,1,0]
a5 = [1,1,1,0,0,0,1,1,0]
a6 = [1,1,1,1,0,0,0,0,1]
a7 = [0,0,0,1,0,0,1,0,1]
a8 = [1,1,1,1,0,1,1,1,0]
a9 = [1,1,1,0,0,1,1,1,0]

t.penup()
t.goto(-300,0)
for i in a1,a4,a1,a7,a0,a0:
    num(i,50)
    t.forward(50)
import turtle
t = turtle.Turtle()
t.shape('turtle')
t.penup()
for i in range(0,100,5) :
    t.forward(10 + i)
    t.left(30)
    t.stamp()
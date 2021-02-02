import turtle
t = turtle.Turtle()
t.shape('classic')
t.color('green')
t.speed(0)
bg = turtle.Screen()
bg.title('aaaaaaaaa')
for a in range(10) :
    for i in range(360) :
        t.forward(1)
        t.left(1)
    t.forward(100)
    t.right(36)
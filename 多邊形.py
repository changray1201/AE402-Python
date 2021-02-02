import turtle
t = turtle.Turtle()
d = 1
t.shape('turtle')
t.color('silver')
n = int(input("輸入邊的個數"))
for i in range(n) :
    t.forward(100)
    t.right(360 / n)
import turtle

t = turtle.Turtle()
s = turtle.Screen()

colors = ["purple", "red", "orange", "yellow", "blue", "magenta", "cyan", "white", "black", "red", "purple"]
s.bgcolor("brown")

t.pensize(2)
t.speed(0)

for x in range(360):
    t.pencolor(colors[x % len(colors)])
    t.width(x // 100 + 1)
    t.forward(x)
    t.right(59)  # ângulo arbitrário para criar o padrão espiralado

t.hideturtle()
turtle.done()

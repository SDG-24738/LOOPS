import turtle
tortise = turtle.Screen()
speed = turtle.Turtle()
colors = ['red', 'orange', 'green', 'blue', 'indigo', 'violet']
tortise.bgcolor('black')
speed.speed('fastest')
speed.hideturtle()
while True:
    for x in range(200):
        speed.pencolor(colors[x%len(colors)])
        speed.width(x/100 + 1)
        speed.forward(x)
        speed.left(59)
    speed.right(239)
    for x in range(100, 0, -1):
        speed.pencolor('black')
        speed.width(x/100 + 7)
        speed.forward(x)
        speed.right(59)
        
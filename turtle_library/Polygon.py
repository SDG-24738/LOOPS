import turtle
turtle.Screen().bgcolor("black")
turtle.Screen().setup(500,500)
polygon = turtle.Turtle() 
num_sides = 10
side_length = 100
angle = 360.0 / num_sides
for x in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()
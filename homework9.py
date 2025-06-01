#This is a program to create 2 wierd squares.
import turtle
import random
l = 200
turtle.pendown
x = turtle.xcor()
y = turtle.ycor()
turtle.speed(0)
for i in range(400):
    turtle.color(random.random(), random.random(), random.random())
    turtle.forward(l)
    turtle.right(90)
    turtle.forward(l)
    turtle.right(90)
    turtle.forward(l)
    turtle.right(90)
    turtle.forward(l)
    turtle.goto(x-2,y-2)
    turtle.right(90)
    l-=1


turtle.done()
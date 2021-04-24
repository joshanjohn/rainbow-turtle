import turtle
mypen = turtle.Turtle()
mypen.shape('turtle')
mypen.speed(10)
window = turtle.Screen()
window.bgcolor('skyblue')
style = ['conrter',50,'italics']
rainbow = ['red','orange','yellow','green','blue','indigo','violet']
size = 200
mypen.penup()
mypen.goto(0,-100)
for color in rainbow:
    mypen.color(color)
    mypen.fillcolor(color)
    mypen.begin_fill()
    mypen.circle(size)
    mypen.end_fill()
    size-=30

mypen.hideturtle()
turtle.done()

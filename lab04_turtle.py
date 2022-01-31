import turtle
wn=turtle.Screen()
ed=turtle.Turtle()

ed.speed('fastest')
ed.pencolor('red')
square=int(input("How many squares to draw?: "))
units=int(input("What unit to increment the length of each side of the square?: "))


for i in range(square*4):
    ed.forward(10)
    ed.right(90)
    units=10+units
    ed.forward(units)
   

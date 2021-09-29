import random
import turtle
import math
a=300
turtle.tracer(2)
turtle.speed(0)
turtle.penup()
turtle.goto(a, a)
turtle.pendown()
turtle.goto(a, -a)
turtle.goto(-a, -a)
turtle.goto(-a, a)
turtle.goto(a, a)
turtle.tracer(50)
number_of_turtles = 25
steps_of_time_number = 10000

dt=0.1
vx=[]
vy=[]
tmp=1
pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.turtlesize(0.2)
    unit.speed(0)
    vx.append((random.random()*8-4))
    vy.append((random.random()*8-4))
    unit.hideturtle()
    unit.goto(random.randint(-a+3, a-3), random.randint(-a+3, a-3) )
    unit.showturtle()

for i in range(steps_of_time_number):
    j=0
    for unit in pool:
        unit.goto(unit.xcor()+vx[j]*dt, unit.ycor()+vy[j]*dt)
  
        if abs(unit.xcor())>a-1:
            vx[j]=-vx[j]
        if abs(unit.ycor())>a-1:
            vy[j]=-vy[j]
        j+=1

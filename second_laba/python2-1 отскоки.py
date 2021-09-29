#тело падает и подскакивает по параболе.
import turtle
turtle.shape('circle')
turtle.speed(0)
turtle.right(90)
turtle.forward(3)
turtle.left(90)
turtle.forward(400)
turtle.backward(700)
turtle.shapesize(0.3)
Vx=15
Vy=50
dt=0.05
a=-10
x=-300
y=0
for i in range (5000):
  turtle.goto(x, y)
  x += Vx*dt
  y += Vy*dt + a*(dt**2)/2
  Vy += a*dt
  if (y<0) and (Vy<0):
      Vy=Vy*(-1/1.4)
      Vx=Vx*0.7

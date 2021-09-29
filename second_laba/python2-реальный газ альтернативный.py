import random
import turtle
import math
a=200
b=a+3
turtle.speed(0)
turtle.penup()
turtle.goto(b, b)
turtle.pendown()
turtle.goto(b, -b)
turtle.goto(-b, -b)
turtle.goto(-b, b)
turtle.goto(b, b)

# нарисовали границу (коробку). 2*а - размер стороны
number_of_particles = 10
steps_of_time_number = 100000
# задали число частиц и итераций
dt=0.05
gamma=0.3
beta=0.1
potential_distance=20
deg=1
frequency=40
#delay=100
turtle.tracer(frequency)
vx=[]
vy=[]
x0=[]
y0=[]
# задали временной шаг
# листы с данными об j-той частице
# постоянную G
# поправочный бета, чтобы не делить на ноль
# задали потенциальное расстояние
pool = [turtle.Turtle(shape='circle') for i in range(number_of_particles)]
for unit in pool:
#    unit.tracer(frequency)
    unit.penup()
    unit.turtlesize(0.5)
    unit.speed(0)
    vx.append((random.random()*4-2))
    vy.append((random.random()*4-2))
    unit.hideturtle()
    tmpx=random.randint(-a+3, a-3)
    tmpy=random.randint(-a+3, a-3)
    unit.goto(tmpx, tmpy)
    unit.showturtle()
    x0.append(tmpx)
    y0.append(tmpy)
# однократно раскидали частицы по объему
# задали каждой начальную скорость по обеим координатам
# записали в листы данные о каждой частице

for i in range(steps_of_time_number):
#    sumspeeds=0
#    if i%100==0:
#        for s in range (len(vx)):
#            sumspeeds+=(vx[s]**2+vy[s]**2)**0.5
#        print(sumspeeds, '\n')
    for unit in pool:
        unit.goto(unit.xcor()+vx[pool.index(unit)]*dt, unit.ycor()+vy[pool.index(unit)]*dt)
        x0[pool.index(unit)]+=vx[pool.index(unit)]*dt
        y0[pool.index(unit)]+=vy[pool.index(unit)]*dt
        if abs(unit.xcor())>a-2:
            vx[pool.index(unit)]=-vx[pool.index(unit)]
        if abs(unit.ycor())>a-2:
            vy[pool.index(unit)]=-vy[pool.index(unit)]
# рассчитываем смещение каждой частицы на каждом шагу
# если она зашла за стенку, разворачиваем по соответствующей координате
# далее попарно сравниваем координаты всех частиц, если они попали в потенциальное расстояние - меняем скорости
    for unit in pool:
        for i in range(number_of_particles):
            if (unit.distance(x0[i]+vx[i]*dt, y0[i]+vy[i]*dt) < potential_distance):
                if unit.xcor()<x0[i]:
                    vx[pool.index(unit)]-=gamma/(abs(unit.xcor()-x0[i])**deg+beta)
                elif unit.xcor()>x0[i]:
                    vx[pool.index(unit)]+=gamma/(abs(unit.xcor()-x0[i])**deg+beta)
                if unit.ycor()<y0[i]:
                    vy[pool.index(unit)]-=gamma/(abs(unit.ycor()-y0[i])**deg+beta)
                elif unit.ycor()>y0[i]:
                    vy[pool.index(unit)]+=gamma/(abs(unit.ycor()-y0[i])**deg+beta)
            
            

from turtle import *

k = 50
screensize(2000, 2000)
tracer(0)
left(90)
down()

for i in range(2):
    forward(9*k)
    right(90)
    forward(15*k)
    right(90)

up()

forward(12*k)
right(90)

down()

for i in range(2):
    forward(6*k)
    right(90)
    forward(12*k)
    right(90)

up()

for x in range(-50, 51):
    for y in range(-50, 51):
        setpos(x*k, y*k)
        dot(5)

done()
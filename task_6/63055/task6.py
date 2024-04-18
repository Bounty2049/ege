from turtle import *

k = 60
screensize(2000, 2000)
tracer(0)
left(90)
down()

for i in range(4):
    forward(12*k)
    right(90)
for i in range(5):
    forward(4*k)
    right(45)

up()

for x in range(-50, 51):
    for y in range(-50, 51):
        setpos(x*k, y*k)
        dot(5)

done()
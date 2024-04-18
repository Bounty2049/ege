from turtle import *

k = 30

screensize(2000, 2000)
tracer(0)

left(90)

down()
l = 8
for i in range(5):
    forward(l*k)
    right(90)
    forward(3*k)

up()

for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x*k, y*k)
        dot(5)

done()
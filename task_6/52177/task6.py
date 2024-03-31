from turtle import *

k = 40
screensize(2000, 2000)
tracer(0)

left(90)

for i in range(4):
    forward(6 * k)
    right(90)
    forward(6 * k)
    left(90)
    forward(6 * k)
    right(90)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x*k, y*k)
        dot(5)

done()
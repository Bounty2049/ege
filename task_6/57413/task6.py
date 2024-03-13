from turtle import *

tracer(0)
screensize(2000, 2000)
k = 30

left(90)
right(45)

for i in range(7):
    forward(5*k)
    right(45)
    forward(10*k)
    right(135)

penup()

for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x*k, y*k)
        dot(5)

done()
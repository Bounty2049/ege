from turtle import *

tracer(0)
k = 30
screensize(5000, 5000)
left(90)

x = int(input())
for i in range(4):
    forward(x*k)
    right(90)
    forward(x*k)
    left(90)
    forward(x*k)
    right(90)

penup()

for x in range(-100, 100):
    for y in range(-30, 30):
        setpos(x*k, y*k)
        dot(5)

done()
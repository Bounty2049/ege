from math import sqrt


for y in range(0, 39):
    for x in range(0, 39):
        if ((5 * 39 ** 8) + (8 * 39 ** 7) + (x * 39 ** 6) + (7 * 39 ** 5) + (2 * 39 ** 4) + (3 * 39 ** 3) + (y * 39 * 2) + (4 * 39 * 1) + 9) % 38 and (y*39**1+x)**0.5==round((y*39**1+x)**0.5):
            print(y*39**1+x)
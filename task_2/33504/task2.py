print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(((x == (not(y))) <= (y and (not(z)))) or (z and (not(w)))):
                    print(x, y, z, w)


# 0 0 1 0
# 1 0 - 0
# - 1 - 0

# wzxy
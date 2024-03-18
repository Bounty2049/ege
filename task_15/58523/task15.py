p = list(range(13, 32))
q = list(range(18, 81))
r = list(range(48, 115))
a = []
for x in range(0, 100):
    if not(not((x in q) <= ((x in p) or (x in r)))) <= ((not(x in a)) <= (not(x in q))):
        a.append(x)

print(a)
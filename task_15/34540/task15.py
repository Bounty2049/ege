p = range(12, 63)
q = range(52, 92)
a = []

for x in range(0, 100):
    if not(not(not(x in a) and (x in p)) or (x in q)):
        a.append(x)

print(a)
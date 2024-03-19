p = list(range(10, 36))
q = list(range(17, 49))
a = list(range(0, 100))
for x in range(0, 100):
    if not(((x in a) <= (not(x in p))) <= ((x in a) <= (x in q))):
        a.remove(x)

print(a)
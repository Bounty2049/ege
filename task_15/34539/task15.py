p = list(range(22, 73))
q = list(range(42, 103))
a = []
for x in range(0, 100):
    if not(not((not(x in a)) and (x in p)) or (x in q)):
        a.append(x)

print(a)
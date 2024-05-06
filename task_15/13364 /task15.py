P = [i for i in range(130, 172)]
Q = [i for i in range(150, 186)]
A = []

for x in range(130, 186):
    if not((x in P) <= (((x in Q) and (x not in A)) <= (x not in P))):
        break
    else:
        A.append(x)

print(A)
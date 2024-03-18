P = list(range(5, 31))
Q = list(range(14, 24))
A = list(range(1, 100))
for x in range(1, 100):
    if not(((x in P) == (x in Q)) <= (not(x in A))):
        A.remove(x)

print(A)
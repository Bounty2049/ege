p=range(4, 16)
q=range(12,20)
A=[int(i) for i in range(1,16)]
for x in range(100):
    if (((x in p) and ((x in q))) <= (x in A)):
        A=A[1:]
    else:
        print(len(A))
f = open('17.txt', encoding='utf-8')
A = [int(i) for i in f]

max19 = max([x for x in A if abs(x) % 100 == 19])

maxi = count = 0
for i in range(len(A) - 2):
    a = A[i]
    b = A[i + 1]
    c = A[i + 2]
    sumboolean = [len(str(abs(x))) == 4 for x in [a, b, c]]
    if sum(sumboolean) == 2:
        if any(x % 3 == 0 for x in [a, b, c]):
            if (a + b + c) > max19:
                count += 1
                maxi = max(maxi, a + b + c)

print(count, maxi)

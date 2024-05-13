A = [int(x) for x in open('1777.txt', encoding='utf-8')]

max29 = max([x for x in A if abs(x) % 100 == 29])

cnt = 0
maxi = -10 ** 101
for i in range(len(A) - 2):
    a, b, c = A[i], A[i + 1], A[i + 2]

    sumboolean = [len(str(abs(x))) == 5 for x in [a, b, c]]
    if sum(sumboolean) == 2:
        if (a + b + c) <= max29:
            cnt += 1
            maxi = max(maxi, a + b + c)


print(cnt, maxi)


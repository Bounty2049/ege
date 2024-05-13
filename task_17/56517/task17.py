A = [int(x) for x in open('17.txt', encoding='utf-8')]

min3 = min([x for x in A if abs(x) % 10 == 3])

cnt = 0
maxi = -10 ** 101

for i in range(len(A) - 1):
    if abs(A[i]) % 10 == abs(A[i + 1]) % 10:
        if sum([x % 3 == 0 for x in [A[i], A[i + 1]]]) == 1:
            if (A[i] ** 2 + A[i + 1] ** 2) <= min3 ** 2:
                cnt += 1
                maxi = max(maxi, A[i] ** 2 + A[i + 1] ** 2)

print(cnt, maxi) 

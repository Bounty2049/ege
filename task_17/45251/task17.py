A = [int(x) for x in open('107_17.txt', encoding='utf-8')]

min21 = min([x for x in A if x % 21 == 0])

cnt = maxi = 0
for i in range(len(A) - 1):
    if any(x % min21 == 0 for x in [A[i], A[i + 1]]):
        cnt += 1
        maxi = max(maxi, A[i] + A[i + 1])


print(cnt, maxi)

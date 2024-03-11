f = open('./9_1.txt', encoding='utf-8')
cnt = 0

for i in f:
    l = sorted(int(x) for x in i.split())
    if (l[0] * 6 < sum(l) - l[0]) and (l[0] * l[3] > l[1] * l[2]):
        cnt += 1

print(cnt)
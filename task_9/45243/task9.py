f = open('9.txt', encoding='utf-8')
cnt = 0

for i in f:
    l = sorted([int(x) for x in i.split()])
    if (l[0] + l[-1]) ** 2 > l[1] ** 2 + l[2] ** 2 + l[3] ** 2:
        cnt += 1

print(cnt)
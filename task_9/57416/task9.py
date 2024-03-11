f = open('./9_1.txt', encoding='utf-8')
cnt = 0

for i in f:
    l = sorted(int(x) for x in i.split())
    if len(set(l)) == len(l):
        x = min(l)
        y = max(l)
        if sum([x, y]) * 2 <= sum(l) - x - y:
            cnt += 1

print(cnt)

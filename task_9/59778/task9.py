f = open('./9_1.txt', encoding='utf-8')
cnt = 0

for i in f:
    l = sorted(int(x) for x in i.split())
    if len(set(l)) == 4:
        rep = [x for x in l if l.count(x) > 1]
        non_rep = [x for x in l if l.count(x) == 1]
        if sum(non_rep) / len(non_rep) > sum(rep):
            cnt += 1
print(cnt)
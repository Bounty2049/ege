codenumoftask = (63058, 59802, 59779, 38943, 46967)

f = open('9_2024', 'r', encoding='utf-8')
cnt = 0
for i in f:
    l = sorted(int(x) for x in i.split())
    if len(set(l)) == 5:
        rep = [x for x in l if l.count(x) == 2]
        non_rep = [x for x in l if l.count(x) == 1]
        if sum(rep) / len(rep) < sum(non_rep) / len(non_rep):
            cnt += 1
print(cnt)

# f = open('9_2024', 'r', encoding='utf-8')
# cnt = 0
# for i in f:
#     l = sorted(int(x) for x in i.split())
#     if l[0] + l[1] < l[2] or l[0] + l[1] < l[3]:
#         cnt += 1
# print(cnt)

# f = open('9_2024', 'r', encoding='utf-8')
# cnt = 0
# for i in f:
#     l = sorted(int(x) for x in i.split())
#     if l[0] ** 2 + l[1] ** 2 > l[2] ** 2:
#         cnt += 1
# print(cnt)

# f = open('9_2024', 'r', encoding='utf-8')
# cnt = 0
# for i in f:
#     l = sorted(int(x) for x in i.split())
#     if len(set(l)) == 4:
#         rep = [x for x in l if l.count(x) > 1]
#         non_rep = [x for x in l if l.count(x) == 1]
#         if sum(rep) / len(rep) > sum(non_rep) / len(non_rep):
#             cnt += 1
# print(cnt)

# f = open('9_2024', 'r', encoding='utf-8')
# cnt = 0
# for i in f:
#     l = sorted(int(x) for x in i.split())
#     rep = [x for x in l if l.count(x) == 2]
#     non_rep = [x for x in l if l.count(x) == 1]
#     if len(set(rep)) == 2:
#         if sum(non_rep) / len(non_rep) < sum(rep) / len(rep):
#             cnt += 1
# print(cnt)

# f = open('9_2024', 'r', encoding='utf-8')
# cnt = 0
# for i in f:
#     l = sorted(int(x) for x in i.split())
#     flag = False
#     if len(l) != len(set(l)) and l.count(max(l)) == 1:
#         flag = True
#     sum_rep = []
#     if flag:
#         for j in l:
#             if l.count(j) > 1:
#                 sum_rep.append(j)
#         if sum(sum_rep) < max(l):
#             cnt += 1
# print(cnt)
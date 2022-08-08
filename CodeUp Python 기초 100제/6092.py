a = int(input())
lst = input().split()

for i in range(0, a):
    lst[i] = int(lst[i])

d = []
for i in range(24):
    d.append(0)

for i in range(a):
    d[lst[i]] += 1

for i in range(1, 24):
    print(d[i], end=' ')

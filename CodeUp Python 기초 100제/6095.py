lis = [[0 for j in range(20)] for i in range(20)]

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(n):
        lis[x][y] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(lis[i][j], end=' ')
    print()

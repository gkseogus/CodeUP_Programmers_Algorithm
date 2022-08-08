lis = [[0 for j in range(20)] for i in range(20)]

n = int(input())

for i in range(n):
    x, y = input().split()
    for j in range(1, 20):
        if lis[j][int(y)] == 0:
            lis[j][int(y)] = 1
        else:
            lis[j][int(y)] = 0

        if lis[int(x)][j] == 0:
            lis[int(x)][j] = 1
        else:
            lis[int(x)][j] = 0
        print(lis[i][j], end='')
    print()

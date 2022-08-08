a, m, d, n = map(int, input().split())

if(-50 <= a, m, d <= 50 and 0 <= n <= 10):
    for i in range(1, n):
        a = a * m + d
    print(a)

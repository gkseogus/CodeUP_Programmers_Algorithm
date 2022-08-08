a, d, n = map(int, input().split())

if( 0<= a,d,n <=100):
    for i in range(1, n):
        a += d
    print(a)

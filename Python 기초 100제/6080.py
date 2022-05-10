a , b = map(int, input().split())

if(a <=10 and b<=10):
    for i in range(1, a+1):
        for j in range(1, b+1):
            print(i,j)

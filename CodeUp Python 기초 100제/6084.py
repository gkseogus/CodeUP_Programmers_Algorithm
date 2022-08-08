h, b, c, s = map(int, input().split())
mb = 0
if ( h<=48000 and (b<=32 and b%8==0) and c<=5 and s<=6000 ):
    mb = h*b*c*(s/8/1024/1024)
    print(round(mb, 1),'MB')
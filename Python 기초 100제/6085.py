w, h, b = map(int, input().split())
mb = 0
if ( 0< w,h < 1025 and (b<=40 and b%4 == 0)):
    mb = w*h*(b/8/1024/1024)
    print('%.2f'%mb,'MB')
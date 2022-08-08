a = int(input())
count = 0
total = 0

if ( 0 <= a < 1001):
    while (total <= a):
        total += count
        if (total >= a):
            print(count)
            break
        else:
            count += 1

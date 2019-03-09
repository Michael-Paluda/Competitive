import time

n = int(input())

for i in range(n):

    count = 0

    digit1, digit2 = map(int, input().split())

    t0 = time.time()

    base = sum([int(i) for i in str(digit1)])

    while digit1 != digit2:
        count += base
        
        digit1 += 1

    count += sum([int(i) for i in str(digit2)])

    print(count)

    t1 = time.time()

    print(t1 - t0)






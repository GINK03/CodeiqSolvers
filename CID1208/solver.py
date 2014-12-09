import sys

for line in sys.stdin:
    a,b = map(int, line.strip().split(' '))
    if a == 0 and b == 0:
        continue
    temp = 1
    for i,_ in enumerate(xrange(b)):
        temp = (lambda x:x%1000000000 if x > 1000000000 else x)(temp)*a
        if i%10000000 == 0:
            pass
    print int(str(temp)[-8:])

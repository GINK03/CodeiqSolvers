import os

stdin = iter(os.read(0, 10000000).splitlines())

N = int(next(stdin))
lines = [int(next(stdin)) for x in xrange(N)]

def fibonacci(r):
    n, n_,tmp = 1, 1, 1
    for _ in xrange(r):
        tmp = n + n_
        n = n_
        n_ = tmp
    return tmp
for line in lines:
#for line in xrange(1,11):
    if line == 0:
        print 0
        continue
    elif line == 1 or line == 2:
        print 1
        continue
    print int(str(fibonacci(line-2))[-3:])

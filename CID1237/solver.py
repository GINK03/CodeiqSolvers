import itertools


def prime_table(n):
    li = [True for _ in xrange(n + 1)]
    i = 2
    while i * i <= n:
        if li[i]:
            j = i + i
            while j <= n:
                li[j] = False
                j += i
        i += 1
    table = [i for i in xrange(n + 1) if li[i] and i >= 2]
    return table

def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n /= i 
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table
for i in xrange(10000, 100000):
    xs = 'X'.join(map(str, prime_decomposition(i)))
    ys = sum(map(int, map(None, str(i))))
    if ys == xs.count('X'):
        print i

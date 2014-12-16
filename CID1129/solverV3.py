import os
import functools

TEST = '''20
12434
657751
151251
805211
1755178
1767886
27720560
40259059
41225425
40850067
86284265
41102465
157079636
234491556
200551464
35743807
20020263
86069783
133288536
49609347'''
#stdin = iter(os.read(0, 10000000).splitlines())
stdin = iter(TEST.splitlines())

N = int(next(stdin))
lines = [int(next(stdin)) for x in range(N)]

#@functools.lru_cache(None)
h = {}
def fibonacci(n):
    if h.get(n):
        return h.get(n)%10000
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    h.update({n:a})
    return a%10000
def resolve_fibonacci(n):
    if n <= 10000:
        return fibonacci(n)
    if n%2 == 1:
        return resolve_fibonacci( (n-1)//2 + 1 )**2 + resolve_fibonacci( (n-1)//2 )**2
    else:
        return resolve_fibonacci( n//2 )*( 2*resolve_fibonacci( n//2 + 1) - resolve_fibonacci( n//2 ))
for line in lines:
    print(int(str(resolve_fibonacci(line))[-3:]))

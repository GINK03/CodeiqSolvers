import os
import itertools
import copy
stdin = iter(os.read(0,1000000).splitlines())

T = [int(x) for x in stdin]
T2 = sorted(copy.copy(T))

class INT:
    c = 0
def isswap(T, t, INT):
    a, b = T[t], T[t+1]
    if a > b:
        INT.c += 1
        T[t], T[t+1] = T[t+1], T[t]


for i in itertools.count(1):
    for t in xrange(len(T) -1):
        isswap(T,t, INT)
    if T == T2:
        break
print INT.c



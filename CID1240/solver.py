import itertools

L = range(1,13)
LT = range(1,13)
c = 0
for l in itertools.permutations(L):
    if filter(lambda x:x[0] == x[1], zip(l,LT)) == []:
        c += 1
print 'res', c

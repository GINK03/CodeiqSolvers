from decimal import *
import itertools

getcontext().prec = 40
L = map(Decimal, range(1,9))

def cal():
    results = []
    for ps in itertools.permutations(L):
        p1, p2, p3, p4, p5, p6, p7, p8 = ps
        res = (p1 + p2**(-1 * (p3 *10 + p4))).ln()
        res2 = (p5**(p6*10+p7) + p8/10)
        results.append( [res*res2, ps] )
        if p1 >= 2:
            break
        #print ps
    print map(int, filter(lambda x:x[0]>0, sorted(map(lambda x:[x[0] - 1, x[1]], results), key=lambda x:x[0])).pop(0).pop())

cal()
def verify():
    import math
    p1, p2, p3, p4, p5, p6, p7, p8 = map(Decimal, [1, 2, 7, 6, 4, 3, 8, 5])
    print ( (p1 + p2**(-1 * (p3 *10 + p4))) ).ln() * (p5 ** (p6 * 10 + p7) + p8/10)

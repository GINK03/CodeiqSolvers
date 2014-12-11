import itertools
import math

for i in xrange(1,11):
    a = math.ceil(i/2.)
    oe = i%2 == 0
    print i, a, oe
    print 'step', (lambda x:x-1 if x > 1 else 1)(i)
    for i_ in xrange(1, i+2, (lambda x:x-2 if x > 2 else 1)(i) ):
        print i_,
    print ''

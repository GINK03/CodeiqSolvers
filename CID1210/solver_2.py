import itertools
import collections
import math
INs = iter([(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)\
    ])

def generateList(counter, i):
    res = []
    for k in counter.keys():
        if counter[k] >= i:
            for _ in xrange(i):
                res.append(k)
        elif counter[k] < i:
            for _ in xrange(counter[k]):
                res.append(k)
    print res
    return res

for data in INs:
    counter = collections.Counter(data)
    setter = set([])
    for i in xrange(1, len(data)+1):
        eval_list = generateList(counter, i)
        for p in itertools.permutations(eval_list, i):
            entry = ','.join(map(str, sorted(p)))
            if not entry in setter:
                setter.add(entry)
    print len(setter)
              

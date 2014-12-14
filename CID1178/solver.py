import itertools
import random
import copy
from compiler.ast import flatten

L = [[0,0,1,0,1],
     [0,0,1,0,1],
     [1,1,0,0,0],
     [0,0,0,1,0],
     [0,1,0,0,0],
     ]

def isNull():
    pass

move = {0:(2,1),
        1:(2,-1),
        2:(1,2),
        3:(-1,2),
        4:(1,-2),
        5:(-1,-2),
        6:(-2,1),
        7:(-2,-1),
        }
for _ in itertools.count(1):
    p = [0,0]
    l = copy.deepcopy(L)
    count = 0
    trace = []
    for i in itertools.count(1):
        deadend = 0
        while True:
            vec = list(move.get(random.randrange(0,8)))
            ptmp = map(lambda x:(p[0] + x[0],p[1] + x[1]), [vec])
            #print random.randrange(0,8)
            pcontext = ptmp.pop()
            if pcontext[0] >= 0 and pcontext[1] >= 0 and pcontext[0] < 5 and  pcontext[1] < 5 and l[pcontext[0]][pcontext[1]]:
                l[pcontext[0]][pcontext[1]] = None
                p[0], p[1] = pcontext[0], pcontext[1]
                count += 1
                trace.append( (vec,pcontext) )
                break
            if pcontext[0] >= 0 and pcontext[1] >= 0 and pcontext[0] < 5 and  pcontext[1] < 5 and not l[pcontext[0]][pcontext[1]]:
                deadend += 1
                if deadend > 100000:
                    break
                    pass
        if deadend > 100000:
            break
    f = filter(lambda x:x == 1, flatten(l))
    if f == []:
        print 'temp result,', flatten(l), 'num', count, 'trace', trace

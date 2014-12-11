import itertools
h = {
        1:'steal',
        2:'stela',
        3:'telas',
        4:'teals',
        5:'elast',
        6:'least',
        7:'laste',
        8:'astel'
    }

def validation(ps):
    toEval = []
    for p in ps:
        toEval.append(h.get(p))
    res = True
    for y in xrange(0,5):
        may = toEval[0][y] + toEval[1][y] + toEval[2][y] + toEval[3][y] + toEval[4][y] 
        if not may in h.values():
            res = False
    return (res, toEval)

for i,ps in enumerate(itertools.permutations(range(1,9), 5)):
    res, toEval = validation(ps)
    if res:
        print '\n'.join(toEval)
        break


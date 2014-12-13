import collections


h = {
        'A':['B','C','D','E','F','G','J'],
        'B':['A','E','G','H'],
        'C':['A','D','E','G','J'],
        'D':['A','C','H','I'],
        'E':['A','B','C','G','H','J'],
        'F':['A','G','I'],
        'G':['A','B','C','E','F'],
        'H':['B','D','E','I'],
        'I':['D','F','H'],
        'J':['A','C','E'],
    }

hnum = {}
for k,v in h.iteritems():
    hnum.update( {k: len(v)} )

for k, v in h.iteritems():
    for c in xrange(len(v)):
        v[c]  = hnum.get(v[c])
    h[k] = sum(v)
R = sorted([(k,v) for k,v in h.iteritems()], key=lambda x:x[1]).pop()

print R

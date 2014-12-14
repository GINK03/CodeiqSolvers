import itertools;t=range(220,331,10);a=range(0,7);a=a+a;[t.remove(p[0]*50+p[1]*80) if p[0]*50+p[1]*80 in t else 0 for p in itertools.permutations(a,2)];print t

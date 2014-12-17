import copy
for i in xrange(1000, 1, -1):
    s = str(i)
    n = (lambda s:len(s)/2+1 if len(s)%2 == 1 else len(s)/2)(s)
    r = copy.copy(map(None,s[(-1)*n:]))
    r.reverse()
    if map(None,s[:n]) == r:
        print s
        break

def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n /= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table
import collections
h = {}
for i in xrange(2, 306):
    t = dict( collections.Counter( prime_decomposition(i) ) )
    if h.get(i-1):
        for k, v in h.get(i-1).iteritems():
            if t.get(k):
                t[k] += v
            else:
                t[k] = v
    h.update({i:t})
c = 0
for k, vh in h.iteritems():
    two_num = vh.get(2)
    vh[2] = 0
    other_num = sum(vh.values())
    if two_num == other_num:
        c +=1
print c

import itertools
import math
source = [1,2,3,4,5,6,7]
results = []
for ps in itertools.permutations(source):
    a,b,c,d,e,f,g = ps
    results.append( [ math.log(a)*( (b/10.0 + c/10.0)**(-1*d) - e**(-1*(f + g/10.)) ) - 1.,ps] )
print ' '.join(map(str, filter(lambda x:x[0]>0.,sorted(results,key=lambda x:x[0])).pop(0).pop()))

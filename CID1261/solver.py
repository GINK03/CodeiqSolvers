# CID1261
import itertools
from compiler.ast import flatten
Bs = map(str, [1.0, 1.0, 5.0, 8.0] )
OPs = ['+', '-', '*', '/']


for bs in itertools.permutations(Bs,4):
    for o in itertools.product(OPs,repeat=4):
        tgt = flatten(zip(bs, o))
        tgt.pop()
        tgt.insert(2, '(')
        tgt.insert(8, ')')
        tgt_str = ''.join(tgt)
        # insert round( () ) 
        if eval(tgt_str) == 10.0:
            print tgt_str
            break

import math
import itertools
import copy
import random
from compiler.ast import flatten
PSIZE = len('1 6 13 14 9 4 1'.split(' ')) - 1
EVAL = [1,6,13,14,9,4,1]
k = 7
seed = [1]
nextlist = copy.copy(seed)
vertical_list = []
vh_list = []
for v in range(k-1):
    horizon_list = []
    for h in range(len(nextlist)):
        vh_list.append([v+1,h+1])
        if h == 0:
            horizon_list.append(nextlist[h]+0)
        if h== len(nextlist) -1:
            horizon_list.append(nextlist[h]+0)
            vh_list.append([v+1,h+1+1])
            break
        horizon_list.append(nextlist[h] + nextlist[h+1])
    vertical_list.append(horizon_list)
    nextlist = horizon_list
print vertical_list
print vh_list
#make break point
for vh in vh_list:
    pointer = []
    nextlist = copy.copy(seed)
    vertical_list = []
    for v in range(k-1):
        horizon_list = []
        for h in range(len(nextlist)):
            if h == 0:
                horizon_list.append(nextlist[h]+0)
            if h == len(nextlist) -1:
                horizon_list.append(nextlist[h]+0)
                break
            if vh == [v+1,h+1]:
                horizon_list.append(nextlist[h] - nextlist[h+1])
            else:
                horizon_list.append(nextlist[h] + nextlist[h+1])
        vertical_list.append(horizon_list)
        nextlist = horizon_list
    if vertical_list[-1] == EVAL:
        print 'match'
        print vertical_list[-1]
        print vh
        break
    else:
        print vertical_list[-1]


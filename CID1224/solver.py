# CID1224
import copy 
S = [0 for x in range(10)] + [1] + [0 for x in range(10)]
VH = [S]
for v in range(9):
    s = [0 for x in range(21)]
    for h in range(21):
        if h+1 < 21:
            s[h] = VH[-1][h-1] + VH[-1][h+1]
        else:
            s[h] = VH[-1][h-1] + VH[-1][h]
    VH.append(s)

for vh in VH:
    print ''.join(map(lambda x:' ' if x == 0 else str(x), vh))

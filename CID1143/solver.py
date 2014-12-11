#coding: utf-8
P='''A：88
B：92
C：78
D：83
E：91'''
import re
for b in [t[0] + ' : ' + t[1] for t in sorted([(p[0], re.search('(\d{1,})', p).group(1)) for p in P.splitlines()], key=lambda x:x[1])]:
    print b

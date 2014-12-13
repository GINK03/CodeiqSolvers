import collections
import itertools
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
count = 0
for friends in itertools.combinations( h.keys(), 3):
    a, b, c = friends
    if b in h.get(a) and c in h.get(a):
        count += 1
print count 

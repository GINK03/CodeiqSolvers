import itertools

def car(l):
    return l[0]

def cdr(l):
    return l[1:]

def cons(some, l):
    l.insert(0,some)
    return l

def nullp(l):
    if l == []:
        return True
    else:
        return False

def reverse_aux(lsource, ltarget):
    while False == nullp(lsource):
        head = car(lsource)
        cons(head, ltarget)
        lsource = cdr(lsource)

    return ltarget

def reverse2(lsource):
    return reverse_aux(lsource, [])

print cons('X', ['A', 'B', 'C']) 
print reverse_aux( ['A', 'B', 'C', 'D'], ['E', 'F', 'G'] )
print reverse2(['A','B','C','D'])


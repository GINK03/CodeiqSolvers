

def generator():
    n, m = 1, 1
    yield n
    yield m
    while True:
        tmp = n 
        n = n + m
        m = tmp
        yield n

for i,f in enumerate(generator()):
    if f > 500:
        print i+1
        break

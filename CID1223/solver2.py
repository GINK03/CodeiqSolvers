def pascal(x, y):
  if(x == 1 or x == y):
    return 1
  else:
    return pascal(x - 1, y - 1) + pascal(x, y - 1)

def line(n):
    a = []
    for i in range(n):
        a.append(pascal(i, n))
    return a

for i in range(10):
    print line(i+1)

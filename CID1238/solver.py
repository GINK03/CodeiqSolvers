def f(x,y,e):
    return int( (x - y - e)*(x - y + e) < 0 )

if __name__ == '__main__':
    print("%d %d" % (f(2, 4, 1), f(6, 3, 4)))


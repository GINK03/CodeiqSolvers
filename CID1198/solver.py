c = 0
for i in xrange(10, 100):
    head = filter(lambda x:x=='1', map(None, str(bin(i))))
    tail = filter(lambda x:x=='1', map(None, ''.join(map(lambda x:str(bin(int(x))), map(None, str(i))))))
    if head == tail:
        c += 1

print c

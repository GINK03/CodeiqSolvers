
print(','.join([(lambda x:str(x) if x%5 != 0 and x%3 != 0 else (lambda x:'Fizz Buzz' if x%15 == 0 else (lambda x:'Fizz' if x%3 == 0 else (lambda x:'Buzz' if x%5 == 0 else None)(x) )(x))(x))(x) for x in xrange(1,101)]))

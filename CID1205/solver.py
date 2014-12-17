# you need to buy 280yen-ticket at least 7.
# minimam amount 15-tickets
res = []
for t280 in xrange(0,7+1):
    for t82 in xrange(0,15+1):
        for t52 in xrange(0,15+1):
            for t10 in xrange(0,15+1):
                for t2 in xrange(0,15+1):
                    for t1 in xrange(0,15+1):
                        s = sum(map(lambda x:x[0]*x[1], zip([1,2,10,52,82,280],[t1,t2,t10,t52,t82,t280])))
                        if s == 2007:
                            res.append([sum([t1,t2,t10,t52,t82,t280]), (t1,t2,t10,t52,t82,t280)])
print sorted(res,key=lambda x:x[0])[:5]

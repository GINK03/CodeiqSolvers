import urllib
import random
allrange = 0
def search(db = 1, index = 0, ans = 208050656559285601386927895421059705239114932023754):
    global allrange
    url = 'http://salvageon.textfile.org/?'
    params = urllib.urlencode({'db':db, 'index':index})
    response = urllib.urlopen(url + params)
    context = response.read()
    try:
        key, allrange = int(context.split(' ')[2][1:]), int(context.split(' ')[-1])
    except:
        print 'may except', context
    return (context, allrange, key)

maxie = 2155006020387989982544395440
minie = 1901475900342344102245054800
def bindGenerator():
    global maxie
    global minie
    while True:
        #yield random.randint(minie, maxie)
        yield random.randint(minie, maxie)
# search rules
import sys
TGT =2023636070998557444542586045 
DB = 2
context, allrange, key = search(DB, 0, TGT)
MINI = 12676506002282294014967032053


firstList = [allrange/1000*n for n in xrange(1,1001) ]
#firstList = [12676506002282294014967032053/100*n for n in xrange(1,101) ]
#print firstList, allrange

for f in firstList:
    context, allrange, key = search(DB, f, TGT)
    print 'differ', f, '\t', TGT - key
sys.exit(0)

banlist = []
renzoku = 0
for i in bindGenerator():
    context, allrange, key = search(DB, i, TGT)
    if i in banlist:
        renzoku += 1
        if renzoku < 20:
            continue
        maxie = 2155006020387989982544395440
        minie = 1901475900342344102245054800
        renzoku = 0
        print 'dispose this trial'

    print TGT, i, '\t', key, allrange
    if key > TGT:
        maxie = i
        banlist.append(key)
    elif TGT > key:
        minie = i
        banlist.append(key)
    else:
        print 'ans', context
        break

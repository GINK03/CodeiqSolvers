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

maxie = 1
minie = 0
def bindGenerator():
    global maxie
    global minie
    while True:
        #yield random.randint(minie, maxie)
        yield random.randint(minie, maxie)
# search rules
TGT = 208050656559285601386927895421059705239114932023754
for i in bindGenerator():
    context, allrange, key = search(DB, i, TGT)
    print TGT, i, key, allrange
    if maxie == 1:
        maxie = allrange
    if key > TGT:
        maxie = i
    elif TGT > key:
        minie = i
    else:
        print 'ans', context
        break

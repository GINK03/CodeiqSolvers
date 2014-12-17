import math
import decimal
def prime_table(T):
  factfilter = [True for _ in xrange(T.sqrt()-10*7, T.sqrt())]
  i = T.sqrt()-10*7
  while i * i <= n:
    if factfilter[i]:
      j = i + i
      while j <= n:
        factfilter[j] = False
        j += i
    i += 1
  table = [i for i in xrange(T.sqrt()-10*7, T.sqrt()) if factfilter[i] and i >= 2]
  return table


decimal.getcontext().prec = 100
T = decimal.Decimal(114381625757888867669235779976146612010218296721242362562561842935706935245733897830597123563958705058989075147599290026879543541)
def it():
    maxx = T.sqrt()
    while True:
        yield maxx
        maxx -= 1

for n,i in enumerate(it()):
    if n%10000000 == 0:
        print 'iter',n
    if T%i == 0:
        print 'prime is,',i
        break

import math
import decimal
def prime_table(n):
  list = [True for _ in xrange(n + 1)]
  i = 2
  while i * i <= n:
    if list[i]:
      j = i + i
      while j <= n:
        list[j] = False
        j += i
    i += 1
  table = [i for i in xrange(n + 1) if list[i] and i >= 2]
  return table



decimal.getcontext().prec = 100
T = decimal.Decimal(114381625757888867669235779976146612010218296721242362562561842935706935245733897830597123563958705058989075147599290026879543541)
def it():
    maxx = T.sqrt()
    while True:
        yield maxx
        maxx -= 1

for n,i in enumerate(it()):
    if n%1000000 == 0:
        print 'iter',n
    if T%i == 0:
        print 'prime is,',i
        break

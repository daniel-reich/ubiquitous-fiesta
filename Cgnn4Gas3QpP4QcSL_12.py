
from itertools import islice
def sum_digits_in_range(n):
  def gen():
    n,x = 0, 45
    yield 0
    yield x
    while True:
      n+=1
      x = 10*x + 45*10**(n)
      yield x
      
  g = gen()
  return list(islice(g,n,n+1))[0]


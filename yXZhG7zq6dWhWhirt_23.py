
def filter_primes(num):
  b = [[x for x in range(1, max(num)+1) if n%x==0] for i, n in enumerate(num)]
  return [num[i] for i, x in enumerate(b) if len(x) == 2]


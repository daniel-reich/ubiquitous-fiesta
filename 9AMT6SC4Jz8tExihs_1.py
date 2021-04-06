
def generate_nonconsecutive(n):
  b = lambda d: bin(d)[2:].zfill(n)
  return ' '.join([b(x) for x in range(2**n) if '11' not in b(x)])


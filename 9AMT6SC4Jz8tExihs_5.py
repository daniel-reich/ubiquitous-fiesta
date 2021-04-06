
from itertools import product
def generate_nonconsecutive(n):
  meh = [''.join(str(b) for b in bits) for bits in product(*(([0,1],)*n))]
  return ' '.join(m for m in meh if '11' not in m)


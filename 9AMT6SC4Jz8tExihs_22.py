
def generate_nonconsecutive(n):
  fmt = '{:0%db}' % n
  binums = (fmt.format(i) for i in range(2**n))
  return ' '.join(i for i in binums if '11' not in i)


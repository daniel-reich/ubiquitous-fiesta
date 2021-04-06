
def construct_fence(p):
  p = int(p.replace(',', '')[1:])
  return 'H' * (1000000//p)


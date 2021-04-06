
def construct_fence(p):
  p = int(p[1:].replace(',',''))
  return 'H' * (1000000 // p)


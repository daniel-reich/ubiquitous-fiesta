
def construct_fence(p):
  np = p.strip('$').replace(',','')
  count = 1000000 // int(np)
  return 'H' * count


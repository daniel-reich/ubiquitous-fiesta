
def construct_fence(p):
  p = p.replace(',','')
  return 1000000 // int(p.replace('$','')) * 'H'


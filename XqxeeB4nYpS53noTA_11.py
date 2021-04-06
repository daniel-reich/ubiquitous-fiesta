
def construct_fence(p):
  p=p[1:]
  p=p.replace(',',"")
  return 'H'*(1000000//int(p))


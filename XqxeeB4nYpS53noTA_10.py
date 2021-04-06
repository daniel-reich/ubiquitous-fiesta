
def construct_fence(p):
  num = "".join([i for i in p if i.isdigit()])
  f = 1000000//int(num)
  return 'H'*f


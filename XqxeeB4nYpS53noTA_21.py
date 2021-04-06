
def construct_fence(p):
  a=''
  for i in p:
    if i.isdigit():
      a+=i
  return 'H'*(1000000//int(a))


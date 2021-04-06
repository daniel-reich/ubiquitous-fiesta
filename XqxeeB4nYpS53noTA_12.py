
def construct_fence(p):
  b = ''
  for x in str(p)[1:]:
    if x != ',':
      b = b + x
  c = int(b)
  return 'H' * (1000000 // c)


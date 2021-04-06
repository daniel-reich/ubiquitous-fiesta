
def construct_fence(p):
  return 'H' * (1000000//int(''.join(ch for ch in p if ch.isdigit())))


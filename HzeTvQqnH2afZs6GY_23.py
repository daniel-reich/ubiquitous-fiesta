
def generate_rug(n, direction):
  rug = [list(range(i,0,-1)) + list(range(n-i)) for i in range(n)]
  return rug if direction=='left' else list(reversed(rug))


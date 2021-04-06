
def generate_rug(n, direction):
  direction=1 if direction=='left'else -1
  origin = [i for i in range(n)][::direction]
  return [[abs(i-j) for i in origin] for j in range(n)]


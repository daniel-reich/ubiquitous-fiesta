
def pop(state):
  n = len(state)//2
  return [n - abs(n - i) for i in range(len(state))]


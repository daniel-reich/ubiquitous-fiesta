
def pop(state):
  d = list(range(len(state)//2))
  return d + [len(state)//2] + d[::-1]


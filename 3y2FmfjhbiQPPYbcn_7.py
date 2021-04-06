
def pop(state):
  return [min(i, len(state) - i - 1) for i in range(len(state))]


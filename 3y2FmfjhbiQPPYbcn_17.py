
def pop(state):
  if max(state) == 0:
    return state
  else:
    return list(range(0, max(state))) + [max(state)] + list(range(0, max(state)))[::-1]


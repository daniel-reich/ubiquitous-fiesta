
def pop(state):
  pop, vol = find_pop(state)
  if vol == 0: return state
  i = 1
  for x in range(vol-1,0,-1):
    state[pop+i] = x
    state[pop-i] = x
    i += 1
  return state
​
def find_pop(state):
  for i in state:
    if i != 0: return (state.index(i),i)
  return (0,0)



def pop(state):
  halth = [x for x in range(len(state)//2+1)]
  return halth + halth[:-1][::-1]


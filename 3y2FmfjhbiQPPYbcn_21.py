
def pop(state):
  if state==[0]:return [0]
  p=[i for  i in range(len(state)) if state[i]!=0][0]
  return [i if i<=p else p*2-i for i in range(len(state))]



def final_direction(initial, turns):
  dir={'L':-1,'R':1}
  comp={'N':0,'E':1,'S':2,'W':3}
  s=sum([dir[i] for i in turns])
  d=(comp[initial]+s)%4
  return ''.join([x for x in comp if comp[x]==d])


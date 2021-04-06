
def final_direction(initial, turns):
  for x in range(len(turns)):
    if initial== 'N':
      if turns[x]=='L':
        initial ='W'
      if turns[x]=='R':
        initial='E'
    elif initial== 'E':
      if turns[x]=='L':
        initial = 'N'
      if turns[x]=='R':
        initial='S'
    elif initial== 'S':
      if turns[x]=='L':
        initial = 'E'
      if turns[x]=='R':
        initial='W'
    elif initial== 'W':
      if turns[x]=='L':
        initial = 'S'
      if turns[x]=='R':
        initial='N'
  return initial


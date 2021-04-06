
def final_direction(initial, turns):
  d = {'N': 'WE', 'E': 'NS', 'S': 'EW', 'W': 'SN'}
  for t in turns:
    initial = d[initial][0] if t == 'L' else d[initial][1]
  return initial



def final_direction(initial, turns):
  l = ['W', 'N', 'E', 'S']
  i = l.index(initial)
  return l[(i + sum(1 if x == 'R' else -1 for x in turns))%4]


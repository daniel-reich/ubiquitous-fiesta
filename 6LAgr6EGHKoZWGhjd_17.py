
DIR_DICT = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
def final_direction(initial, turns):
  p = DIR_DICT[initial]
  for i in turns:
    if i == 'L':
      p -= 1
    else:
      p += 1
  if p < 0:
    p += 4
  else:
    p = p % 4
  t = list(DIR_DICT.keys())[list(DIR_DICT.values()).index(p)]
  return t


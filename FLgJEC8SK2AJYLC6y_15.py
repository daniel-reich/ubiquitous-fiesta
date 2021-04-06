
def possible_path(lst):
  paths = {1:[2], 2:[1,'H'], 'H':[2,4], 4:[3,'H'], 3:[4]}
  current = lst[0]
  for next_move in lst:
    options = paths[current]
    if next_move in options or next_move == current:
        current = next_move
    else:
      return False
  return True


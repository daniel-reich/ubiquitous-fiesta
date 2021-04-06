
def shortest_path(lst):
  target = 2
  times_moved = 0
  
  # Finds co-ords of all targets
  targets = {}
  for y, row in enumerate(lst):
    for x, col in enumerate(row):
      if col is not '0':
        targets[int(col)] = [x+1, y+1]
  
  # Finds number of moves (With no obsticals)
  while target in targets.keys():
    pos, tar_pos = targets[(target-1)], targets[target]
    
    times_moved += abs(abs(pos[0]-tar_pos[0]) + abs(pos[1]-tar_pos[1]))
    target += 1
    
  # Terribly inefficient
  return times_moved


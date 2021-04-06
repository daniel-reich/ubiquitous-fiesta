
def track_robot(instructions):
  pos = [0, 0]
  for instruction in instructions:
    split = instruction.split()
    pos = move(split[0], int(split[1]), pos)
  return pos
  
def move(dir, qty, curr):
  if dir == "left":
    curr[0] -= qty
  elif dir == "right":
    curr[0] += qty
  elif dir == "up":
    curr[1] += qty
  elif dir == "down":
    curr[1] -= qty
  return curr


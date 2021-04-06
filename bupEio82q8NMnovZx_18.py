
def track_robot(instructions):
  result = [0,0]
  for move in instructions:   
    if "right" in  move:
      result[0] += int(move.split(" ")[1])
    elif "left" in move:
      result[0] -= int(move.split(" ")[1])
    elif "up" in move:
      result[1] += int(move.split(" ")[1])
    elif "down" in  move:
      result[1] -= int(move.split(" ")[1])
  return result


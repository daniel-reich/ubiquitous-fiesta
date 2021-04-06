
def track_robot(instructions):
  if len(instructions) == 0:
    return [0,0]
  direction = [0]*len(instructions)
  for i in range(len(instructions)):
    if instructions[i].split()[0] == 'right':
      direction[i] = [int(instructions[i].split()[1]), 0]
    elif instructions[i].split()[0] == 'left':
      direction[i] = [-int(instructions[i].split()[1]), 0]
    elif instructions[i].split()[0] == 'up':
      direction[i] = [0, int(instructions[i].split()[1])]
    elif instructions[i].split()[0] == 'down':
      direction[i] = [0, -int(instructions[i].split()[1])]
  return [sum(x) for x in zip(*direction)]

